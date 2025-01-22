from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now


from core.models import PublishedModel, CreatedAtModel, TitleModel


User = get_user_model()


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'category',
            'author',
            'location',
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=now(),
        )


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=True,
            created_at__lte=now(),
        )


class LocationManager(models.Manager):
    pass


class Post(PublishedModel, CreatedAtModel, TitleModel):
    text = models.TextField(
        blank=False,
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        blank=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время '
        'в будущем — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Категория',
    )
    objects = PostManager()

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Category(PublishedModel, CreatedAtModel, TitleModel):
    description = models.TextField(
        blank=False,
        verbose_name='Описание',
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    objects = CategoryManager()

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel, CreatedAtModel):
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Название места',
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
