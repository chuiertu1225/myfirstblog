
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import User


class Login(APIView):
    def post(self,request):
        password = request.data.get('pwd')
        print(request.data)
        user = request.data.get('user')
        print(user)
        a = User.objects.filter(username=user).count()
        print(a)
        if a:
            return Response({
                "code":20000,
                "msg":'success'
            })
        return Response({
            "code":20000,
            "msg":'fail'
        })
