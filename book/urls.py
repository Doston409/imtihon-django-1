from django.urls import path
from . import views

urlpatterns = [
    path('Book/', views.Book_page, name='Book_page'),
    path('create/', views.create_page, name='create_page')
]