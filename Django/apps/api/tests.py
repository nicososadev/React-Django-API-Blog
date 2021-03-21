from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status, test

from apps.blog.models import Blog, Category

User = get_user_model()

class BlogTest(test.APITestCase):

    def test_blog_list(self):
        url = reverse('api:blog-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_create(self):
        self.test_category = Category.objects.create(name='testCategory')
        self.test_user = User.objects.create_user(username='testUser', password='123456')

        self.client.login(username=self.test_user.username, password='123456')

        blog_data = {
            'title': 'testBlog',
            'category': 1,
            'author': 1,
            'content': 'testContent'
        }

        url = reverse('api:blog-list')
        response = self.client.post(url, blog_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_blog_update(self):

        client = test.APIClient()

        self.test_category = Category.objects.create(name='testCategory')
        self.test_user = User.objects.create_user(username='testUser', password='123456')
        self.test_user2 = User.objects.create_user(username='testUser2', password='123456')

        self.test_blog = Blog.objects.create(title='testBlog', category_id=1, author_id=1, content='testBlogContent')

        url = reverse('api:blog-detail', kwargs={'pk': 1})

        blog_update_data = {
            'title': 'testUpdateBlog',
            'category': 1,
            'author': 1,
            'content': 'testUpdateBlogContent'
        }

        # Only author can update

        client.login(username=self.test_user.username, password='123456')

        response = client.put(url, blog_update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        client.logout()

        # Another user can not update

        client.login(username=self.test_user2.username, password='123456')

        response = client.put(url, blog_update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

