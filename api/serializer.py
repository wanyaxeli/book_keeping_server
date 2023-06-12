from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User,Store,Sales,Reciepts,Trash
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    def validate_password(self,value):
        if value is not None :
            return make_password(value)
     
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Store
        fields='__all__'
        read_only_fields = ('user',)
        def validate(self, data):
            if self.instance and self.instance.user != self.context['request'].user:
                raise serializers.ValidationError("You are not authorized to access this store.") 
            return data

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields='__all__'
        read_only_fields = ('user',)
    def validate(self, data):
            if self.instance and self.instance.user != self.context['request'].user:
                raise serializers.ValidationError("You are not authorized to access this store.") 
            return data

class ReceiptsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reciepts
        fields='__all__'
        read_only_fields = ('user',)
    def validate(self, data):
            if self.instance and self.instance.user != self.context['request'].user:
                raise serializers.ValidationError("You are not authorized to access this store.") 
            return data

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trash
        fields='__all__'
        read_only_fields = ('user',)
    def validate(self, data):
            if self.instance and self.instance.user != self.context['request'].user:
                raise serializers.ValidationError("You are not authorized to access this store.") 
            return data