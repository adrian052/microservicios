from django.shortcuts import render

from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets, status

class ProductViewSet(viewsets.ViewSet):
    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de mensajes
        orders = Product.objects.all()
        # Se crea el serializer y se envía como response
        serializer = ProductSerializer(orders, many=True)
        
        return Response(serializer.data)

    def retrive(self,request,pk):
        item = Product.objects.get(id=pk)
        serializer = ProductSerializer(item)
        return Response(serializer.data)

    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self,request,pk):
        order = Product.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        # Se obtiene la lista de mensajes
        categoria = Category.objects.all()
        # Se crea el serializer y se envía como response
        serializer = CategorySerializer(categoria, many=True)
        return Response(serializer.data)

    def retrive(self,request,pk):
        item = Category.objects.get(id=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = CategorySerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self,request,pk):
        categoria = Category.objects.get(id=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)