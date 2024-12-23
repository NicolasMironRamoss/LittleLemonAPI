from django.urls import path
from . import views

url_patterns = [path('menu-items', views.MenuItemsView.as_view()),]