from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, ListField, IntegerField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import MyUser


class MyUserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user

    """ def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance """
    
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