from django.shortcuts import render
from django.http import Http404

from blog.models import Post


def post_list(request):
    posts = Post.objects.all()

    return render(request, "blog/post/list.html", {"posts": posts})

def post_detail(request, id):
    try:
        post = Post.approved.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post found')
    return render(request, 'blog/post/detail.html',{'post':post})