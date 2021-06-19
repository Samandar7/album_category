from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category, Photo

# Create your views here.


class HomePageView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'kategoriya'

class ListView(ListView):
    model = Photo
    template_name = 'list.html'
    context_object_name = 'list'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'detail.html'
    context_object_name = 'view'

