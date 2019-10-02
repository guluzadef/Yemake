from django.contrib import admin
from .models import *
from image_cropping import ImageCroppingMixin

# Register your models here.
admin.site.register(Site_name)
admin.site.register(Menu)
admin.site.register(Main)
admin.site.register(First)
admin.site.register(Second)
admin.site.register(Footer)
@admin.register(Meals)
class MealsmodelAdmin(ImageCroppingMixin,admin.ModelAdmin):
    fields = ['name','author','category']
admin.site.register(Photos_Pages)
admin.site.register(Texts_Pages)
# admin.site.register()

