from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


        
""" lst = [
        'Misha123', '55667788', 'Михаил', 
        'Маджоров', 'мужской', '25', 'админ'       
    ]
def encode():
    model = UserModel(lst)
    model_sr = UserSerializer (model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

class UserModel:
    lst = [
        'login', 'password', 'first_name', 
        'last_name', 'gender', 'age', 'post'       
    ]
    def __init__(self, lst):
        self.login = lst[0]
        self.password = lst[1]
        self.first_name = lst[2]
        self.last_name = lst[3]
        self.gender = lst[4]
        self.age = lst[5]
        self.post = lst[6] """

""" class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'first_name', 'last_name')

class SubtestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtest
        fields = ('name', 'test_id')
 """