from django.contrib import admin

from django.contrib import admin
from .models import Article
# Article 클래스를 admin 페이지에 등록
admin.site.register(Article)
# Register your models here.
