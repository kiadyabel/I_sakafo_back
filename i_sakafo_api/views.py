from django.shortcuts import render
from .models import Blog , Category
from .serializers import BlogSerializer ,CategorySerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
# Create your views here.

class BlogApiView(viewsets.GenericViewSet , mixins.ListModelMixin , mixins.RetrieveModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field ='slug'
    


class CategoryApiView(viewsets.GenericViewSet , mixins.ListModelMixin , mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field ='id'
    
class CategoryPostApiView(viewsets.ViewSet):
    def retriev(self , request , pk = None):
        queryset = Blog.objects.filter(category=pk)
        serialzer = BlogSerializer(queryset, many = True)
        return Response(serialzer.data)