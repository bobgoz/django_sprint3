from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.db.models import Q

from blog.models import Post, Category


def index(request):
    post_list = Post.objects.select_related(
        'category',
        'author',
        'location',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now()
    ).order_by(
        '-pub_date',
    )[0:5]

    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.filter(
        Q(is_published=True)
        & Q(category__is_published=True)
        & Q(pub_date__lte=now())),
        id=post_id)

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(
        is_published=True,
        created_at__lte=now()),
        slug=category_slug)

    post_list = Post.objects.select_related(
        'category',
        'author',
        'location',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now(),
        category__slug=category_slug
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
