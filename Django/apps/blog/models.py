from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):

    STATUS_OPTIONS = (
        ('published', 'Publicado'),
        ('notPublished', 'No Publicado')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(max_length=250, verbose_name='Contenido')
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Publicado')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    status = models.CharField(max_length=12, choices=STATUS_OPTIONS, default='notPublished', verbose_name='Estado')

    class PublishedBlogsManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    publishedBlogs = PublishedBlogsManager()
    objects = models.Manager()

    class Meta:
        verbose_name = ('blog')
        verbose_name_plural = ('blogs')
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
