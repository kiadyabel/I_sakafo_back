from django.urls import path , include 
from .views import BlogApiView , CategoryApiView, CategoryPostApiView 
from rest_framework import routers

router = routers.SimpleRouter()

router.register('blogs', BlogApiView , basename = 'blogs')
router.register('category', CategoryApiView , basename = 'category')
router.register('categoryBasedblogs', CategoryPostApiView , basename = 'categoryBasedblogs')


urlpatterns = [
    path('',include(router.urls))
] 