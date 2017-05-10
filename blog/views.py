from django.shortcuts import render

# Very simple view to be seen, accessed by urls.py which calls post_list
def post_list(request):
    # post_list.html will be accessed by this
    return render(request, 'blog/post_list.html', {})


