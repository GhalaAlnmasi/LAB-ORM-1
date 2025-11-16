from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateField(auto_now_add = True)
    image = models.ImageField(upload_to="movies/images", null=True, blank=True)