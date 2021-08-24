from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_bookdata_from_web


class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filter_fields = ['title', 'published_date']
    ordering_fields = ['published_date']

    def get_queryset(self):
        if self.request.query_params.get('author'):
            authors = self.request.query_params.getlist('author')
            values = []
            for author in authors:
                if author[0] and author[-1] == '"':
                    author = author[1:-1]
                values.append("['"+author+"']")
            return Book.objects.filter(authors__in=values)
        else:
            return self.queryset


class BookView(generics.RetrieveAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(id=self.kwargs['pk'])
        if queryset.exists():
            return queryset


class LoadData(APIView):

    def post(self, request):

        q = request.data.get('q')
        if q == "war":
            Book.objects.all().delete()
            books = get_bookdata_from_web(q)
            for record in books:
                if Book.objects.filter(id=record.get('id')).count() == 0:
                    serializer = BookSerializer(data=record)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response(books, status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
