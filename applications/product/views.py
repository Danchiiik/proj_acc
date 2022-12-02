from django.shortcuts import render
from rest_framework.generics import *

from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from rest_framework.permissions import *


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

# class ProductListApiView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
    
# class ProductCreateApiView(CreateAPIView):
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
    
    
# class ProductDetailApiView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
class ProductRetUpdDelApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
        

