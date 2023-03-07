from django import forms
from apps.models import ContactUs
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields =[
             'name',
             'contact' ,
             'email' ,
             'messages' ,
        ]