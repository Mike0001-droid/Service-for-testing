from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from users.serializers import MyUserSerializer, MyTokenObtainPairSerializer
from users.models import MyUser
from users.schemas import UserSchema
from django.shortcuts import get_object_or_404
import jwt
from drf.settings import SECRET_KEY
from datetime import datetime
PermissionClass = IsAuthenticated  # if not settings.DEBUG else AllowAny


class MyTokenObtainPairView(TokenObtainPairView):
    
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer
    
class MyUserViewSet(ViewSet):
    """
    list:
        Авторизированный пользователь
    create_user:
        Создание пользователя
    update_user:
        Обновление пользователей
    """
    schema = UserSchema()
    def list(self, request):
        serializer = MyUserSerializer(request.user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    @action(detail=False, methods=['post'])
    def update_user(self, request):
        user = MyUser.objects.get(pk=request.user.pk)
        if 'old_password' in request.data:
            if user.check_password(request.data['old_password']):
                if 'password' in request.data:
                    request.data['password'] = make_password(request.data['password'])
                serializer = MyUserSerializer(request.user, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"error": "Неправильный старый пароль"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Введите старый пароль"})
        
    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            text_error = ''
            for error in serializer.errors:
                elm_error = serializer.errors.get(error)
                if len(elm_error) > 0:
                    text_error += "{}".format(elm_error[0])
            return Response({"detail": text_error}, status=status.HTTP_400_BAD_REQUEST)
        token_data = {
            "email": request.data["email"],
            "password": request.data["password"]
        }
        token_serializer = MyTokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        elif self.action == "create_user":
            permission_classes = [AllowAny]
        elif self.action == "update_user":
            permission_classes = [IsAuthenticated]
        elif self.action == "password_reset_user":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
