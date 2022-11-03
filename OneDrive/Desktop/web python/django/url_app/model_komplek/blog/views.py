from django.shortcuts import render

# Create your views here.
from .models import Data

def index(request):
    post = Data.objects.all()

    context = {
        'judul': 'Blog',
        'heading': 'Selamat datang',
        'postingan': post
    }

    return render(request, 'blog/index.html', context)