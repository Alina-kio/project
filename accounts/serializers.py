from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from .models import CustomUser

# # class UserRegistrationSerializer(serializers.ModelSerializer):
# #     email = serializers.EmailField(
# #         required=True,
# #         validators=[UniqueValidator(queryset=CustomUser.objects.all())]
# #     )
# #     username = serializers.CharField(
# #         max_length=30,
# #         validators=[UniqueValidator(queryset=CustomUser.objects.all())]
# #     )
# #     password = serializers.CharField(min_length=8, write_only=True)
# #     confirm_password = serializers.CharField(min_length=8, write_only=True)

# #     class Meta:
# #         model = CustomUser
# #         fields = ('email', 'username', 'password', 'confirm_password')

# #     def validate(self, data):
# #         if data['password'] != data['confirm_password']:
# #             raise serializers.ValidationError("Passwords do not match.")
# #         return data

# #     def create(self, validated_data):
# #         validated_data.pop('confirm_password')
# #         user = CustomUser.objects.create_user(**validated_data)
# #         return user



# # class UserLoginSerializer(serializers.Serializer):
# #     email = serializers.EmailField()
# #     password = serializers.CharField(write_only=True)

# #     def validate(self, data):
# #         email = data.get('email')
# #         password = data.get('password')

# #         if email and password:
# #             user = authenticate(email=email, password=password)
# #             if not user:
# #                 raise serializers.ValidationError("Incorrect email or password.")
# #         else:
# #             raise serializers.ValidationError("Must include 'email' and 'password'.")

# #         data['user'] = user
# #         return data




# from rest_framework import serializers
# from .models import CustomUser
# from django.contrib.auth import authenticate
# # import re

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'username', 'password']
    
#     def validate_email(self, value):
#         if CustomUser.objects.filter(email=value).exists():
#             raise serializers.ValidationError("This email is already in use.")
#         return value
    
#     def validate_password(self, value):
#         if len(value) < 5:
#             raise serializers.ValidationError("Password must be at least 5 characters long.")
    
#         # if not re.search(r'\d', value) or not re.search(r'[a-zA-Z]', value):
#         #     raise serializers.ValidationError("Password must contain both letters and numbers.")
#         # return value

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             password=validated_data['password']
#         )
#         return user
    


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
