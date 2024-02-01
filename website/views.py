from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from website.forms import NameForm,ContactForm,NewsletterForm
from website.models import Contact
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


class SplashView(TemplateView):
    	template_name = "503.html"

def my_view(request):
    return render(request,'503.html') 
   

def index_view(request):
    return render(request,'website/index.html') 

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method=="POST" :
          form= ContactForm(request.POST, request.FILES)
          if form.is_valid():
              form.instance.name='unknown'
              form.save()
              messages.add_message(request,messages.SUCCESS,'your ticked submited successfully')   
          else:
               messages.add_message(request,messages.ERROR,'your ticked did not submited')
               
    form= ContactForm( )
    return render (request,'website/contact.html',{'form':form})


def newsletter_view(request):
      if request.method=="POST" :
          form= NewsletterForm(request.POST)
          if form.is_valid():
             form.save()
          return HttpResponseRedirect('/')
      else: 
          return HttpResponseRedirect('/')
    
          



def test_view(request):
    if request.method=="POST" :
      form= ContactForm(request.POST)
      if form.is_valid():
          form.save()
          return HttpResponse('done')
      else: 
          return HttpResponse('not valid')
    form=  ContactForm()
    return render (request,'test.html',{'form':form})