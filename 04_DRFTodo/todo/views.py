from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSimpleSerializer

class TodosAPIView(APIView):
    def get(self, requeset):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    