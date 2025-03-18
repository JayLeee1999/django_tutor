from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)
    