from django.shortcuts import render
from django.views.generic import ListView
from .models import Bookmark
from django.urls import reverse_lazy
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields=[
        'site_name','url',
    ]
    success_url=reverse_lazy('list')
    template_name_suffix='_create'

class BookmarkUpdateView(UpdateView):
    model=Bookmark
    fields=['site_name', 'url']
    template_name_suffix='_update'

class BookmarkDetailView(DetailView):
    model=Bookmark

class BookmarkDeleteView(DeleteView):
    model=Bookmark
    success_url=reverse_lazy('list')