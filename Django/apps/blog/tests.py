from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.blog.models import Blog, Category

User = get_user_model()

class CreateBlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='test')
        test_user = User.objects.create_user(username='userTest', password='123456')
        test_blog = Blog.objects.create(category_id=1, title='BlogTitle', content='BlogContent', author_id='1', status='published')

    def test_BlogContent(self):
        blog = Blog.publishedBlogs.get(id=1)
        category = Category.objects.get(id=1)
        
        title=blog.title
        content=blog.content
        author=blog.author.username
        status=blog.status

        self.assertEqual(author, 'userTest')
        self.assertEqual(title, 'BlogTitle')
        self.assertEqual(content, 'BlogContent')
        self.assertEqual(status, 'published')
        self.assertEqual(str(blog), 'BlogTitle')
        self.assertEqual(str(category), 'test')
