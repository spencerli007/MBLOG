from django.shortcuts import render, redirect
from .models          import Post
from datetime         import datetime

def homepage(request):
    queryset_list = Post.objects.all()
    now           = datetime.now()
    context = {
        'posts' : queryset_list,
        'now'   : now,
    }
    return render(request, 'index.html', context)

def showpost(request, slug):
    try: 
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
    
