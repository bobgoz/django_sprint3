from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def index(request):
    post_list = Post.posts_objects.order_by('-pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post.posts_objects.all(), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.category_objects.all(),
        slug=category_slug
    )
    post_list = Post.posts_objects.filter(
        category=category,
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
