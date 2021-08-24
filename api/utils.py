import requests

def get_bookdata_from_web(dataset_name):
    url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    # url = 'https://www.googleapis.com/books/v1/volumes?q=war'
    r = requests.get(url)
    books = r.json()['items']
    books_data = []
    for data in books:
        volume_info = data.get('volumeInfo')
        id = data.get('id')
        book_info = dict(id=id,
                        title=volume_info.get('title'),
                        authors=volume_info.get('authors'),
                        published_date=volume_info.get('publishedDate'),
                        categories=volume_info.get('categories'),
                        average_rating=volume_info.get('averageRating'),
                        thumbnail=volume_info.get('thumbnail'))
        book_info_without_none = {k: str(v) for k, v in book_info.items() if v is not None}
        books_data.append(book_info_without_none)
    return books_data