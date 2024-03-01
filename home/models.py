from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField
#https://pypi.org/project/django-tinymce/
#https://github.com/MaistrenkoAnton/django-material-admin

#catagory
class catagory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description=RichTextField()
    url=models.CharField(max_length=200)
    image=models.ImageField(upload_to='catagory/',null=True)
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" /img>'.format(self.image))
    #add_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title
    
        

class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=256)
    content=RichTextField()
    url=models.CharField(max_length=200)
    image=models.ImageField(upload_to='post/',null=True)
    cat=models.ForeignKey(catagory,on_delete=models.CASCADE)
    

    
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" /img>'.format(self.image))
    #add_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title


