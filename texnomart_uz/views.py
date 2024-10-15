from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Product, Image, Order, Comment, AttributeKey, AttributeValue, ProductAttribute
from .serializers import (
    CategorySerializer, ProductSerializer, ImageSerializer,
    OrderSerializer, CommentSerializer, AttributeKeySerializer,
    AttributeValueSerializer, ProductAttributeSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class AttributeKeyViewSet(viewsets.ModelViewSet):
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer

class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer

class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
