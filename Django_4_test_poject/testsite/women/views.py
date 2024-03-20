from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from .forms import AddPostForm
from .models import Women, Category, TagPost

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

class Myclass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Create your views here.
def index(request): #HttpRequest
    # t= render_to_string('women/index.html')
    # return HttpResponse(t)
    post = Women.published.all().select_related('cat')

    data = {'title': 'Главная страница',
            'menu': menu,
            # 'float': 56.56,
            # 'lst': [1, 2, 'abc', True],
            # 'set': {1, 2, 3, 4, 5},
            # 'dict': {'key_1':'value_1', 'key_2': 'value_2'},
            # 'obj': Myclass(10, 20),
            # 'url': slugify("The Main Page"),
            'posts': post,
            'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


# def categories(request, cat_id):
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")
#
#
# def categories_by_slug(request, cat_slug):
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")
#
# def archive(request, year):
#     if year > 2024:
#         uri = reverse('cats_slug', args=('sport',))
#         return HttpResponsePermanentRedirect(uri)
#
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{year}</p>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data ={
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'women/post.html', data)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'women/addpage.html', data)

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {'title': f'Рубрика:{category.name}',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.women.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)




