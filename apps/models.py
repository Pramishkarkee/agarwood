from django.db import models
from apps.baseModel import BaseModel
# Create your models here.

class ContactUs(BaseModel):
    name = models.CharField(max_length=200,blank=True)
    contact = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    messages = models.CharField(max_length=500,blank=True)

# class Tree(BaseModel):
#     contact = models.ForeignKey(ContactUs,on_delete=models.CASCADE)
#     treeType = models.CharField(max_length=50,blank=True)
#     total_tree = models.IntegerField()

class BlogWriter(BaseModel):
    name = models.CharField(max_length=100)
    profile = models.ImageField()
    def __str__(self):
        return self.name

class Blog(BaseModel):
    writer = models.ForeignKey(BlogWriter,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    content = models.TextField()


class Product(BaseModel):
    name = models.CharField(max_length=200)
    picture = models.ImageField()
    feature = models.BooleanField(default=False)


class Testimonial(BaseModel):
    TESTIMONEAL_TYPE=(
        ("CUSTOMER","customer"),
    )
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    type = models.CharField(choices=TESTIMONEAL_TYPE,max_length=30)
    content = models.TextField()
