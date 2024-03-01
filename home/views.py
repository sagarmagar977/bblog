from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    posts=post.objects.all()[:11]
    # print(posts)
    data={ 
        "posts": posts 
        }
    return render(request, 'home.html',data)

def Post(request,url):
    Post=post.objects.get(url=url) 
    #print(Post)
    return render(request,'posts.html', {'post':Post})

