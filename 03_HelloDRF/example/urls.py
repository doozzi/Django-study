from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),   # 함수형 뷰의 booksAPI 연결
    path("fbv/book/<int:bid>/", bookAPI),   # 함수형 뷰의 bookAPI 연결
    path("cbv/books/", BooksAPI.as_view()),     # 클래스형 뷰 BooksAPI 연결
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
]