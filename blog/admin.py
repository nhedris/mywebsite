from django.contrib import admin
from blog.models import Post,category,Comment
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display=['title','counted_views','status','author','login_require','published_date','created_date']
    list_filter=('status','author')
    search_fields=['title','content']
    summernote_fields = ('content',)
    empty_value_display = '-empty-'
    date_hierarchy ='created_date'

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = 'Null'
    list_display=['name','post','approved','created_date']
    list_filter=('post','approved',)
    search_fields=['name','post']
    
admin.site.register(Comment,CommentAdmin)        
admin.site.register(Post,PostAdmin)
admin.site.register(category)