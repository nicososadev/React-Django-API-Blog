from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API
    path('api/', include('apps.api.urls', namespace='api')),

    # Blog
    path('', include('apps.blog.urls', namespace='blog'))
]
