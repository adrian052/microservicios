from django.shortcuts import render

from rest_framework.response import Response
from .models import Order,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework import viewsets,status

class OrderViewSet(viewsets.ViewSet):
    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de mensajes
        orders = Order.objects.all()
        # Se crea el serializer y se envía como response
        serializer = OrderSerializer(orders, many=True)
        
        return Response(serializer.data)

    ##para el create.
    ##{
    ##    "first_name": "Adrian",
    ##    "last_name": "Ibarra",
    ##    "email": "a_drian1@hotmail.es",
    ##    "address": "5 de Mayo #70",
    ##    "postal_code": "99800",
    ##    "city": "Zacatecas",
    ##    "paid": true
    ##} 
    def create(self,request):
        serializer = OrderSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def destroy(self,request,pk):
        order = Order.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemViewSet(viewsets.ViewSet):
    ##{
    ##"product_id": 99,
    ##"price": "1999.00",
    ##"quantity": 2,
    ##"order": 1
    ##}
    def create(self,request):
        print(request.data)
        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self,request,pk):
        item = OrderItem.objects.get(id=pk)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)
