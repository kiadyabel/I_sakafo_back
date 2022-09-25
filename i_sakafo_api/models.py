from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    
    POST_CHOICES = [
        ('POPULAR','popular')
    ]
    
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null= True)
    title = models.CharField(max_length=255)
    slug =models.SlugField(max_length=255)
    excerpt = models.CharField(max_length=255 , default = '')
    content = models.TextField(null=True ,blank = True)
    contentTwo =  models.TextField(null=True ,blank = True)  
    image = models.ImageField(upload_to='images', null= True, blank = True)
    ingredients = models.TextField(null=True , blank=True)
    postLabel = models.CharField(max_length=255 , choices =POST_CHOICES)
    
    def __str__(self):
        return self.title