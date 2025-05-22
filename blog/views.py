from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from django.contrib import messages
from django.db import IntegrityError
from .models import Post, Category
import json
# Create your views here.
def post_create(request):
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                post = form.save(commit=False)

                if request.user.groups.filter(name='Doctor').exists():
                    post.created_by = request.user
                else:
                    raise IntegrityError('You are Not Authorised to Perform this action')
                
                post.save()
                messages.success(request,'Post uploaded successfully!!')
                return redirect('post_detail',id=post.pk)
            except IntegrityError as e:
                messages.error(request, str(e)+" .Kindly re-upload the image if necessary")
                return render(request, 'blog/postform.html', {'form':form})
        else:
            messages.error(request," .Kindly re-upload the image if necessary")
            return render(request, 'blog/postform.html', {'form':form})

    form = PostModelForm()
    return render(request, 'blog/postform.html',{'form':form})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/postdetail.html',{'post':post})


def post_update(request, id):
    print(id)
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('post_detail', id=post.pk)

    form = PostModelForm(instance=post)
    return render(request, 'blog/postform.html', {'form': form})

def post_lists(request):
    if request.user.groups.filter(name='Patient').exists():
        posts = Post.objects.select_related('category').filter(is_draft=False)
    elif request.path == '/blog/posts/drafts':
        posts = Post.objects.select_related('category').filter(is_draft=True,created_by=request.user)
    else:
        posts = Post.objects.select_related('category').filter(is_draft=False,created_by=request.user)

    categories = Category.objects.all()

    post_data = [
        {
            'id': post.id,
            'title': post.title,
            'category': post.category.name if post.category else None,
            'summary': truncate_summary(post.summary),
            'image_url': post.image.url,
        }
        for post in posts
    ]
    
    return render(request,'blog/posts.html',{'categories':categories,'posts_json':json.dumps(post_data)})

def truncate_summary(summary):
    len_summary = len(summary.split(' '))
    if len_summary <= 15:
        return summary
    else:
        lst = summary.split(' ')
        lst = [lst[i] for i in range(15)]
        new_summary = ' '.join(lst)
        return new_summary + '...'
