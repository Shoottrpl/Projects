from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'), # http://127.0.0.1:8000/women/
    path('about/', views.about, name='about'),
    # path('cats/<int:cat_id>/', views.categories, name='cats_id'), # http://127.0.0.1:8000/cats/1/
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),  # http://127.0.0.1:8000/cats/absdfg/
    # path('archive/<year4:year>/', views.archive, name='archive'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>', views.show_tag_postlist, name='tag'),

]
