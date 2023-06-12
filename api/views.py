from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer,StoreSerializer,SalesSerializer,ReceiptsSerializer,TrashSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import User,Store,Sales,Reciepts,Trash
from .permission import OnlyOwnerCanView
# Create your views here.
class UserView(APIView):
    permission_classes=[permissions.AllowAny]
    def post (self,request):
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors)
    
    def get (self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)

class StoreVeiw(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        user = request.user  # Get the user details from the request
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)  # Set the user details in the serializer during creation
            return Response(serializer.data)
        return Response(serializer.errors,)
       
    def get(self,request):
        user=request.user
        store=Store.objects.filter(user=user).order_by('medicine')
        serializer=StoreSerializer(store,many=True)
        return Response (serializer.data)
    
class SalesVeiw(APIView):
        permission_classes=[permissions.IsAuthenticated]
        def post(self,request):
            data=request.data
            user=request.user
            serializer=SalesSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data)
            return Response(serializer.errors)
        def get(self,request):
            user=request.user
            store=Sales.objects.filter(user=user)
            serializer=SalesSerializer(store,many=True)
            return Response (serializer.data)
        

        def delete(self,request,*args,**kwargs):
            pk=self.kwargs['pk']
            todo=Sales.objects.get(pk=pk)
            todo.delete()
            return Response('item deleted')

class ReceiptsVeiw(APIView):
    permission_classes=[permissions.AllowAny]
    parser_classes=[MultiPartParser]
    def post(self,request):
        data=request.data
        user=request.user
        file=request.data['file']
        serializer=ReceiptsSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self,request):
        user=request.user
        store=Reciepts.objects.filter(user=user)
        serializer=ReceiptsSerializer(store,many=True)
        return Response (serializer.data)
    
class TrashVeiw(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def post(self,request):
        user=request.user
        data=request.data
        serializer=TrashSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self,request):
        user=request.user
        store=Trash.objects.filter(user=user)
        serializer=TrashSerializer(store,many=True)
        return Response (serializer.data)