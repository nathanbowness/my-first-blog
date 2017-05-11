from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Very simple view to be seen, accessed by urls.py which calls post_list
def post_list(request):
    # post_list.html will be accessed by this

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
