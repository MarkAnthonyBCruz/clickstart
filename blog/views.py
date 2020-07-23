from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
from .models import Post, Comment
from django.http import HttpResponseRedirect
import requests
from .forms import CommentForm, SearchForm
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.db.models import Q
import random
from django import template
import requests


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def landing(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/landing.html', context)

def services(request):
    return render(request, 'blog/services.html')

def projects(request):
    return render(request, 'blog/projects.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class SearchListView(ListView):
    template_name = 'blog/home.html'
    model = Post
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs['slug'], self.kwargs['pk']])


    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comment'] = Comment.objects.filter(post=self.kwargs['pk']).order_by('-created_on')
        context['form'] = CommentForm(initial={'active': True, 'post': self.kwargs['pk']})
        context['times'] = range(1, 8)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'images', 'category', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'images']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug, 'pk': self.object.post.pk})

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})

def contact(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Inquiry: ' + " " + message_name + " - " + message_email,
             message,
             message_email,
             ['clickstartcctv@gmail.com'],
        )
        #python -m smtpd -n -c DebuggingServer localhost:1025
        return render(request, 'blog/contactus.html', {'message_name': message_name})

    else:
        return render(request, 'blog/contactus.html', {})





