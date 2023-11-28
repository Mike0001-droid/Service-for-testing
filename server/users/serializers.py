from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, ListField, IntegerField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import MyUser


class MyUserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user

   
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'password', 'name', 'surname', 'age', 'gender')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        token['surname'] = user.surname
        
        return token