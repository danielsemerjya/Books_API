from django.urls import path
from api.views import BookListView, LoadData, BookView

urlpatterns = [
    path('books', BookListView.as_view()),
    path('books/<str:pk>', BookView.as_view()),
    path('db', LoadData.as_view())
]