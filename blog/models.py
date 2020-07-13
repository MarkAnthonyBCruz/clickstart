from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    #we didn't use timezone.now() because we just want to get the value
    images = models.ImageField(blank=True, upload_to='post_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    #on_delete is used when we want to delete content of deleted user


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    comm_images = models.ImageField(blank = True, upload_to='comment_images')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)