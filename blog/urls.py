from django.urls import include, path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, SearchListView, CommentDeleteView

app_name = 'blog'
urlpatterns = [
    path('blog/', PostListView.as_view(), name= 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name= 'user-posts'),
    path('blog/post/<slug:slug>/<int:pk>/', PostDetailView.as_view(), name= 'post_detail'),
    path('blog/post/new/', PostCreateView.as_view(), name='post_create'),
    path('blog/post/<slug:slug>/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('blog/post/<slug:slug>/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('blog/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('about/', views.about, name = 'blog-about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name = 'blog-contact'),
    path('search/', SearchListView.as_view(), name = 'search')
]

# <app>/<model>_<viewtype>.html