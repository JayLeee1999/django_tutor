"""
URL configuration for django_tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from community.views import articlelist, viewdetail, write, index

urlpatterns = [
    path('admin/', admin.site.urls),
    # http ~~ 1:8000/write/
    path('write/', write, name='write'), # path, view의 함수
    path('list/', articlelist, name='list'),
    path('view_detail/<int:num>/', viewdetail, name='detail'),
    path('', index, name='index'),
]
# view_detail/1 > 뒤에 숫자가 계속 바뀐다면.. 문법을 넣으면 됨
# <int 숫자야~ num=1 views 에 있는 num과 같아야해