from rest_framework import serializers
from rest_framework.response import Response
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(required=True,error_messages={'required':'请填写字段'})
    pwd = serializers.CharField(required=True,error_messages={'required':'请填写密码'})
    def validate_pwd(self,pwd):
        if len(pwd)>=6:
            return pwd
        else:
            raise Exception('密码小于6位数', 50012)
