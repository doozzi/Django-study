from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):     # CreateAPIView(generics) 사용 구현
    queryset = User.objects.all()
    serializer_class = RegisterSerializer