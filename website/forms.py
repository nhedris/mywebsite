from django import forms
from website.models import Contact , Newsletter
from django.forms import ModelForm
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    message=forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = Contact
        fields=['name','email','message']
        
         
class NewsletterForm(forms.ModelForm): 
       class Meta:
          model = Newsletter 
          fields='__all__'          