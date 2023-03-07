from django.contrib import admin

from apps.baseAdmin import BaseModelAdmin
from apps.models import ContactUs,Blog,Product,BlogWriter,Testimonial

@admin.register(ContactUs)
class ContactUsAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'id',
        'name',
        'email',
        'contact',
        'messages',
        'created_at'
    )

@admin.register(Blog)
class BlogAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'id',
        'writer',
        'created_at'
    )

@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'id', 
        'name'
    )

@admin.register(BlogWriter)
class BlogWriterAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )

@admin.register(Testimonial)
class TestimonialAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )