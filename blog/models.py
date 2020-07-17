from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY = (('CCTV Cameras', 'CCTV Cameras'), ('Politics','Politics'), ('History', 'History'), ('General News','General News'), ('Technology', 'Technology'), ('Gaming', 'Gaming'))
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    #we didn't use timezone.now() because we just want to get the value
    images = models.ImageField(blank=True, upload_to='post_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    slug = models.SlugField(max_length=255, null=True)
    #on_delete is used when we want to delete content of deleted user
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'slug': self.slug, 'pk': self.pk})

    """def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
    """
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    body = models.TextField(blank=True)
    comm_images = models.ImageField(blank=True, upload_to='comment_images')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

