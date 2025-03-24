from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):

  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='testuser',
      email='test@email.com',
      password='secret'
    )

    # sample blog post
    self.post = Post.objects.create(
      title='Test Title',
      body='Test Body Content',
      author=self.user,
    )

  def test_string_representation(self):
    post = Post(title='A sample title')
    self.assertEqual(str(post), post.title)
  
  def test_post_content(self):
    self.assertEqual(f'{self.post.title}', 'Test Title')
    self.assertEqual(f'{self.post.author}', 'testuser')
    self.assertEqual(f'{self.post.body}', 'Test Body Content')

  def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Test Body Content')
    self.assertTemplateUsed(response, 'home.html')

  def test_post_detail_view(self):
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/100000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'Test Title')
    self.assertTemplateUsed(response, 'post_detail.html')