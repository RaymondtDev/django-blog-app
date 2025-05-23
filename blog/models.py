from django.db import models
from django.urls import reverse

# Create your models here.
# class for blog post

class Post(models.Model):
  title = models.CharField(max_length=200)

  # ForeignKey means a user can be the author of many different blog posts, but one blog post cannot have many authors.
  author = models.ForeignKey(
    'auth.User',
    on_delete = models.CASCADE,
  )

  body = models.TextField()

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])
