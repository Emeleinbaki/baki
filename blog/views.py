from django.shortcuts import render

from blog.models import *


def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.all()
    page = Page.objects.all()
    news = New.objects.filter(is_active=True)[:4]
    # mainpage = MainPage.objects.all()
    album = Album.objects.all()
    albumtwo = Albumtwo.objects.all()
    albumthee = Albumthee.objects.all()
    info = Informations.objects.all()
    block = Block.objects.all()
    # socials = Social.objects.all()
    # photoalbum = PhotoAlbum.objects.all()
    # albumblog = AlbumBlog.objects.all()
    return render(request, 'base.html', locals())


def head(request):
    return render(request, 'about.html')
