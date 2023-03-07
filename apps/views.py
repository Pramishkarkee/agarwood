from django.shortcuts import render
from django.http import HttpResponse
from apps import models
from apps.forms import ContactUsForm
from django.core.paginator import Paginator
# Create your views here.
def Index(request):
    blog = models.Blog.objects.all()
    testimoneal = models.Testimonial.objects.all()
    pblog = Paginator(blog, 2)
    product = models.Product.objects.all()
    p = Paginator(product,3)
    return render(request, 'index.html',{"blog": pblog,"testimoneal": testimoneal,'product':product})

def About(request):
    return render(request, 'about.html')

def Blog(request):
    data = models.Blog.objects.all()
    return render(request, 'blog.html',{'data':data})

def Blogdetail(request,id):
    blog = models.Blog.objects.get(id=id)
    return render(request, 'blogdetail.html',{'blog':blog})
def Contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'contact.html')
    return render(request, 'contact.html')

def Goal(request):
    return render(request, 'goal.html')

def Service(request):
    return render(request, 'service.html')

def Product(request):
    product = models.Product.objects.all()
    return render(request, 'product.html',{"product":product})

def Project(request):
    return render(request, 'project.html')

def Opportunity(request):
    return render(request, 'opportunity.html')