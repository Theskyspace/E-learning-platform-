from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Create your models here.
class Category(models.Model):
    Chapter_Name = models.CharField(max_length=200)
    Description = models.TextField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    standard = models.IntegerField()

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('Chapter_Name', 'parent',)    
        verbose_name_plural = "Categories"     

    def __str__(self):                           
        full_path = [self.Chapter_Name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.Chapter_Name)
            k = k.parent
        return ' -> '.join(full_path[::-1])




class Lecture(models.Model):
    title = models.CharField(max_length=120,unique=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)

    videofile= models.FileField(upload_to='videos/', null=True,blank=True, verbose_name="video",max_length=500)
    assignment = models.FileField(upload_to='assignment/', null=True,blank=True, verbose_name="Assignment",max_length=500)

    
    publish = models.DateField(auto_now=False,auto_now_add=False,)

    def __str__(self):
        return self.title  



    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.title)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]