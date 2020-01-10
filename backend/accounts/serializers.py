import re
from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()
    class Meta:
        model = User
        fields = '__all__'
    def validate_email(self, email):
        reg = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if re.match(reg, email):
            return email
        else:
            raise serializers.ValidationError("邮箱不合法")
    def validate_password_confirm(self, password_confirm):
        if(len(password_confirm)<6):
            raise serializers.ValidationError("密码过短")
        else:
            return password_confirm

    def validate_password(self, password):
        if(len(password)<6):
            raise serializers.ValidationError("密码过短")
        else:
            return password
class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(required=True,error_messages={'required':'请填写字段'})
    pwd = serializers.CharField(required=True,error_messages={'required':'请填写密码'})
    def validate_pwd(self,pwd):
        if len(pwd)>=6:
            return pwd
        else:
            raise serializers.ValidationError("小于6位数")
