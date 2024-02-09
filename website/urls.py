from django.urls import path
from website.views import *
import website.views as websiteviews
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static



app_name='website'




urlpatterns = [
 
    #path('url', 'def_views', 'name') 
    #path('',my_view,name='503'),
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('newsletter',newsletter_view , name='newsletter'),
    path('test', test_view, name='test'),
] 
#if settings.MAINTENANCE_MODE:
#       urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='503.html'), name='503'))
