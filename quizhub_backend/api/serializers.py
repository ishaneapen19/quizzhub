from rest_framework import serializers
from .models import User, Category, Question, Attempt
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password 


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'is_admin']
        read_only_fields = ['id', 'username', 'email', 'is_admin'] 


class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all(), message="A user with that email already exists.")]
    )
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = UserModel
        
        fields = ['username', 'password', 'email', 'is_admin'] 


    def create(self, validated_data):
        is_admin_user = validated_data.get('is_admin', False)
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_admin=is_admin_user,
            is_staff=is_admin_user
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AttemptSerializer(serializers.ModelSerializer):
  
    username = serializers.CharField(source='user.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Attempt
    
        fields = ['id', 'score', 'answers', 'category', 'username', 'category_name', 'timestamp']
        
       
        read_only_fields = ['id', 'user', 'timestamp', 'username', 'category_name']

