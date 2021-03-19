from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from apps.blog.models import Blog, Category

User = get_user_model()

class BlogTest(APITestCase):

    def test_blog_list(self):
        url = reverse('api:blog-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_create(self):
        self.test_category = Category.objects.create(name='testCategory')
        self.test_user = User.objects.create_user(username='testUser', password='123456')

        blog_data = {
            'title': 'testBlog',
            'category': 1,
            'author': 1,
            'content': 'testContent'
        }

        url = reverse('api:blog-list')
        response = self.client.post(url, blog_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
