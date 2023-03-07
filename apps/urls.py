from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.Index,name="index"),
    
    path("blog",views.Blog,name="blog"),
    path("blogdetail/<str:id>/",views.Blogdetail,name="blogdetail"),
    path("about-us",views.About,name="about-us"),
    path("contact",views.Contact,name="contact"),
    path("goal",views.Goal,name="goal"),
    path("service",views.Service,name="service"),
    path("product",views.Product,name="product"),
    path("project",views.Project,name="project"),
    path("opportunity",views.Opportunity,name="opportunity"),
    

]