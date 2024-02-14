from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import user
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        User=user.objects.filter(email=email).first()
        if User is None:
            raise AuthenticationFailed("User not found")
        if not User.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        
        payload={
            'id': User.id,
            # 'exp':datetime.datetime.utcnow().datetime.timedelta(minutes=60)
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response=Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            "jwt":token
        }
        return response
    
class UserView(APIView):
    def get(self,request):
            
        token=request.COOKIES.get('jwt')
        return Response(token)