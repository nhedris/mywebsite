from django import template
from django.db import models
from blog import models
from blog.models import Post


register = template.Library()
 
@register.inclusion_tag('website/website-post.html')
def latesposts():
    posts=Post.objects.filter(status=1).order_by('published_date')
    return { 'posts': posts } 