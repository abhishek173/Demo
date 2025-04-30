from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.



class RegisterUser(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":True,
                "message": "user registered successfully..",
                "data":serializer.data
            })
        return Response({
                "status":False,
                "message": " Invalid data ..",
                "data": serializer.errors
            })


class LoginUser(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            user = authenticate(username=data['username'],password=data['password'])

            if user is None:
                return Response({
                    "status":False,
                    "message": "Invalid Username or Password ..",
                    "data": {}
                })
            
            token,created = Token.objects.get_or_create(user=user)

            return Response({
                    "status":True,
                    "message": "User logged in successfully ..",
                    "data": {
                        "token":token.key
                    }
            })
        
        return Response({
        "status":False,
        "message": " Invalid data ..",
        "data": serializer.errors
    })

