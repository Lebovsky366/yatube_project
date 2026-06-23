from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Post, Group

User = get_user_model()

class PostModelTest(TestCase):
    def test_post_creation(self):
        user = User.objects.create_user(username='testuser')
        post = Post.objects.create(author=user, text='Test text')
        self.assertEqual(post.text, 'Test text')

class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.group = Group.objects.create(title='Test Group', slug='test-group')
        self.post = Post.objects.create(author=self.user, text='Hello', group=self.group)

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')