from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    posts=Post.objects.filter(status=1)
    context={'posts' : posts} 
    return render(request,'blog/blog-home.html',context) 



def blog_single(request,pid):
    post=get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())   
    context={'post' : post} 
    return render(request,'blog/blog-single.html',context)

 

def test (request):
     posts=Post.objects.all()  
     context={'posts' : posts} 
     return render(request,'test.html',context)    
