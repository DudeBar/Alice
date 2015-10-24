from django.contrib import admin

# Register your models here.
from website.models import Gallery, Images

admin.site.register(Gallery)
admin.site.register(Images)