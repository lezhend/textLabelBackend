from rest_framework import serializers
from labelDB.models import Account


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'email', 'phoneNumber', 'password', 'is_active', 'is_superuser', 'accountCreateDate')
    
    def create(self, validated_data):
        '''
        Implement hash algorithm to generate hashed password.
        '''
        account = Account.objects.create_user(**validated_data)
        return account