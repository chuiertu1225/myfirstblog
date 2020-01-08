from rest_framework import serializers
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
            return Response({'code':'50012','msg':'密码格式错误'})
