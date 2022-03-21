
from django.db import models
# from ident.blog.validators import validate_file_extension

class Products(models.Model):
    pass

class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=False, verbose_name='Актуально')

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class New(models.Model):
    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
        ordering = ["-date"]

    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=False,verbose_name="Актуально")



    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class Albumtwo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class Albumthee(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class Block(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=100, verbose_name='Описание')
    is_active = models.BooleanField(default=False, verbose_name='Актуально')

    def __str__(self):
        return self.title

class Informations(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='info', verbose_name='Фото')
    url = models.URLField(verbose_name='Ссылка', default='')
    key = models.ForeignKey(to=Block,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
