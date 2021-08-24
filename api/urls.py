from django.contrib import admin
from django.urls import path, include, re_path
from api.views import BookListView, LoadData, BookView

urlpatterns = [
    path('books', BookListView.as_view()),
    path('books/<int:pk>', BookView.as_view()),
    path('db', LoadData.as_view())
]