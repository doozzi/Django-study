from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404  # get_object_or_404 load
from .models import Book  # 모델 불러오기
from .serializers import BookSerializer  # serializer load

# Create your views here.
# 함수형 뷰
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

@api_view(['GET', 'POST'])
def booksAPI(request):  # /book/
    if request.method == 'GET':
        books = Book.objects.all()  # Book 모델로부터 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True)  # serializer에 전체 데이터를 한번에 집어넣기(직렬화, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data) # POST 요청으로 들어온 데이터를 serializer에 넣기
        
        if serializer.is_valid(): # 유효한 데이터라면
            serializer.save() # 역질렬화를 통해 save(), 모델시리얼라이저의 기본 create() 함수가 동작

            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201메세지를 보내며 성공
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 잘못된 요청

@api_view(['GET'])
def bookAPI(request, bid): # /book/bid/
    book = get_object_or_404(Book, bid=bid)  # bid = id 인 데이터를 Book에서 가져오고, 없으면 404 에러
    serializer = BookSerializer(book)   # serializer 에 데이터 집어넣기(직렬화)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# 클래스형 뷰
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()  # Book 모델로부터 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True)  # serializer에 전체 데이터를 한번에 집어넣기(직렬화, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data) # POST 요청으로 들어온 데이터를 serializer에 넣기
        
        if serializer.is_valid(): # 유효한 데이터라면
            serializer.save() # 역질렬화를 통해 save(), 모델시리얼라이저의 기본 create() 함수가 동작

            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201메세지를 보내며 성공
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 잘못된 요청
    
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)  # bid = id 인 데이터를 Book에서 가져오고, 없으면 404 에러
        serializer = BookSerializer(book)   # serializer 에 데이터 집어넣기(직렬화)
    
        return Response(serializer.data, status=status.HTTP_200_OK)