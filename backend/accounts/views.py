import time
from django.shortcuts import render
import jwt
from rest_framework import generics
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import LoginSerializer, RegisterSerializer, UserSerializer


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.validated_data['user']
                item = User.objects.get(username=user)
            except Exception as e:
                print(e)
                return Response({'code': 50012, 'msg': '用户名不存在'})
            if item.password != serializer.validated_data['pwd']:
                return Response({'code': 50012, 'msg': '密码错误'})
            return self.success_Response(user)
    def success_Response(self,name):
        payload={
            "sub":'blog',
            "name":name,
            "exp":time.time()+1000*60*60*24
        }
        print(payload)
        token = jwt.encode(payload,'blog','HS256')
        data = {
            'token':token
        }
        return Response({'code': 20000, 'data':data,'msg': 'Success'})

class Register(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            if (len(User.objects.filter(username=username, del_state=1))) == 0:
                if serializer.validated_data['password'] == serializer.validated_data['password_confirm']:
                    if email and len(User.objects.filter(email=email, del_state=1)) == 0:
                        User.objects.create(username=username,email=email,password= serializer.validated_data['password'])
                        return Response({'code': 20000, 'msg': '注册成功'})
                    else:
                        return Response({'code': 50012, 'msg': '该邮箱已被注册'})
                else:
                    return Response({'code': 50012, 'msg': '密码不统一'})
            else:
                return Response({'code': 50012, 'msg': '用户名已被占用'})

class GetInfo(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            super().get(serializer.data)

        