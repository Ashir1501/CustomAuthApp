from django.db import models
from authapp.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='post_images')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}-{self.title}'