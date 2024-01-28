from django.shortcuts import render

from blog.forms import BlogEditForm
from blog.models import Blog


def list_views(requests):

    blogs = Blog.objects.all()

    return render(requests, 'blogs.html', {'blogs': blogs})


def detail_views(requests, pk):

    blog = Blog.objects.get(pk=pk)

    return render(requests, 'blog.html', {'blog': blog})


def edit_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == "POST":
        form = BlogEditForm(request.POST, instance=blog)
        if form.is_valid:
            form.save()
    else:
        form = BlogEditForm(instance=blog)




    return render(request, 'edit_blog.html', {'form':form, 'blog':blog})
