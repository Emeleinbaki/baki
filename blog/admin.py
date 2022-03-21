

# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import *

admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(Page)
admin.site.register(New)
admin.site.register(Album)
admin.site.register(Albumtwo)
admin.site.register(Albumthee)
# admin.site.register(Address)
# admin.site.register(Social)
admin.site.register(Block)
admin.site.register(Informations)


