from rest_framework import serializers
from labelDB.models import OriginalFile
from labelDB.models import Account

class OriginalFileSerializers(serializers.ModelSerializer):
    # originalFileOwner = serializers.ReadOnlyField(source='originalFileOwner.username')
    class Meta:
        model = OriginalFile
        fields = ('originalFileName', 'originalFileStatus', 'originalFileText', '')

# class AccountSerializers(serializers.ModelSerializer):
#     originalFile = serializers.PrimaryKeyRelatedField(many=True, queryset=OriginalFile.objects.all())
#     class Meta:
#         model = Account
#         fields = ('userName', 'originalFile')
