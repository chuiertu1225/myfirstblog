from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import LoginSerializer


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        print(serializer.is_valid(raise_exception=True))
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.validated_data['user']
                User.objects.get(username = user)
                return Response({'code':20000,'msg':'Success'})
            except :
                return Response({'code':50012,'msg':'用户名异常'})