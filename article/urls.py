from django.urls import path
from .views import (
    articles_list,
    article_detail,
    article_create,
    article_create_form,
    article_change,
    article_delete
)

app_name = 'article'

urlpatterns = [
    path('', articles_list, name='list'),
    path('article/<slug:slug>/', article_detail, name='detail'),
    path('article/create/', article_create, name='create'),
    path('article/create/form/', article_create_form, name='create-form'),
    path('article/change/<int:pk>/', article_change, name='change-form'),
    path('article/delete/<int:pk>/', article_delete, name='delete'),
]

