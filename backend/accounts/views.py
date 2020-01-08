from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import LoginSerializer


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.validated_data['user']
                item = User.objects.get(username=user)
                if item.password != serializer.validated_data['pwd']:
                    return Response({'code':50012,'msg':'密码错误'})
                return Response({'code':20000,'msg':'Success'})
            except :
                return Response({'code':50012,'msg':'用户名不存在'})
