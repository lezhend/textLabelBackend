from django.shortcuts import render
from labelDB.models import Account
from account_manager.serializers import AccountSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from account_manager.permissions import IsSuperUser
import json

# Create your views here.

class AddAccountView(APIView):
    permission_classes = (IsSuperUser,)
    def post(self, request, format=None):
        '''
        Receive informations of new account, then insert into DB.
        Only none-superuser account can be created here.
        '''
        serializer = AccountSerializers(data=request.data)
        if serializer.is_valid():
            if request.data['is_superuser'] == True:
                return Response('Not authorized to create is_superuser.', status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def requestIsValid(self, reqDataDic):
        '''
        We may validate the request data before contact with DB.
        Since we hope to execute in DB when we have to.
        '''
        pass
