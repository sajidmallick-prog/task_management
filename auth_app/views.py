from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer
from django.contrib.auth.models import Group

class RegisterView(APIView):
    permission_classes = [AllowAny] # Allow anyone to register 
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Assigning the default 'User' role as required 
            user_group, _ = Group.objects.get_or_create(name='User')
            user.groups.add(user_group)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)