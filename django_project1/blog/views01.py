from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {"author":"Made Yuda",
     "title":"Blog post 1",
     "content":"First post content",
     "date_posted":"March, 7 2022"
     },
     {"author":"Gede Ahimsa",
     "title":"Blog post 2",
     "content":"Second post content",
     "date_posted":"March, 8 2022"
     },
]
def home(request):
    context = {
        "posts":posts,
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html",{"title":"About Page - Myd"})