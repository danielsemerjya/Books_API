from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_bookdata_from_web


class LoadData(APIView):

    def post(self, request):
        Book.objects.all().delete()
        data = request.data['q']
        if data == "war":
            books = get_bookdata_from_web(data)
            for record in books:
                if Book.objects.filter(title=record.get('title'),
                        published_date=record.get('published_date')).count() == 0:
                    serializer = BookSerializer(data=record)
                    if serializer.is_valid():
                        serializer.save()
                        print('Nowy wpis')
        return Response(status=status.HTTP_200_OK)


class BookView(generics.RetrieveAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])


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
                values.append("['"+author+"']")
            return Book.objects.filter(authors__in=values)
        else:
            return self.queryset