from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=255)
    #author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content= models.TextField()
    #tags = TaggableManager()
    #image=models.ImageField(upload_to='blog/')
    #category=models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    login_require=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField( null=True)
    
    class Meta:
        ordering=['created_date']
        
    def __str__(self):
        return self.title