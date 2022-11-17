from rest_framework import serializers


##New Code
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
##New Code

from django.contrib.auth.models import User
from attendence.models import Attendence, Category




# Video
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = '__all__'
#Video



        
        

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ('id','s_name', 'student_id','user', 'content', 'category','created', 'modified')



# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



## New Code
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer

'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
'''

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
##New Code