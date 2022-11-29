from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken

from applications.account.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response

class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response('You have been saved well. \n We have sent you activation code', status=201)



class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer