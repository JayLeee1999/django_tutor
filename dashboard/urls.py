
from django.urls import path

from dashboard.views import dashboard

app_name = 'dashboard' # community:list
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'), # path, view의 함수
]