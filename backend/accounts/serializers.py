from rest_framework import serializers
from rest_framework.response import Response
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(required=True,error_messages={'required':'请填写字段'})
    pwd = serializers.CharField(required=True,min_length=6,error_messages={'required':'请填写密码',
                                                                          'min_length':'密码不能少于6个字符'})
    def validated_pwd(self,pwd):
        if len(str)>=6:
            return pwd
        else:
            return Response({'code':'50012','msg':'密码格式错误'})
