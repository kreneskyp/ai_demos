from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CatMeme

class MemeListView(ListView):
    model = CatMeme
    template_name = 'memes/meme_list.html'
    context_object_name = 'memes'

class MemeDetailView(DetailView):
    model = CatMeme
    template_name = 'memes/meme_detail.html'
    context_object_name = 'meme'
