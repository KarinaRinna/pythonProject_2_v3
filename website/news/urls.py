from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'), # тут отслеживаем url 'create' в /news (10 строка в website/urls.py)
]
