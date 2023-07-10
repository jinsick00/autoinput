from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Comment
from .forms import PostForm
# Create your views here.

def board_index(request):
    board_list = Post.objects.order_by('-id')
    context = {"board_list" : board_list}
    return render(request, "board/board_list.html", context)

def board_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post" : post}
    return render(request, "board/board_detail.html", context)


def board_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('board:index')
        
    else:
        form = PostForm()
    context = {'form': form}

    return render(request, "board/board_write.html", context)