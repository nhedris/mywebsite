from django.contrib import admin
from blog.models import Post,category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','counted_views','status','author','login_require','published_date','created_date']
    list_filter=('status','author')
    search_fields=['title','content']
    summernote_fields = ('content',)
    empty_value_display = '-empty-'
    date_hierarchy ='created_date'


admin.site.register(Post,PostAdmin)
admin.site.register(category)