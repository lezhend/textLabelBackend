from labelDB.models import OriginalFile
from file_manager.serializers import OriginalFileSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from file_manager.permissions import IsSuperUser
import json

# Create your views here.

class AddOriginalFileView(APIView):
    permission_classes = (IsSuperUser,)
    def post(self, request, format=None):
        '''
        Receive information of new original file to label, then inser into DB.
        '''
        serializer = OriginalFileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, seralizer):
    #     seralizer.save(originalFileOwner=self.request.user)
