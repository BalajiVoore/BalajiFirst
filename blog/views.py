from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.
def blogs(request):
    blo=blog.objects
    return render(request,'blog/blogs.html',{'blogs':blo})
def details(request,blog_id):
    blogdetail=get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/details.html',{'blogger':blogdetail})

