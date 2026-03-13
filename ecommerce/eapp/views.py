from django.shortcuts import render
from .models import Post


# Create your views here.
def eapp_list(request):
    eapp = Post.objects.all().order_by('-date')
    return render(request, 'eapp/eapp_list.html', {'eapp': eapp})

def eapp_pages(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "eapp/post_pages.html", {"post": post})
        