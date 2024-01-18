from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
 
    #path('url', 'def_views', 'name') 
    path('', blog_view,name='index'),
    path('single',blog_single,name='single'),
    
] 