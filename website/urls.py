from django.urls import path
from .views import http_test

urlpatterns = [
 
    #path('url', 'def_views', 'name') 
    path('http-test',http_test)
] 