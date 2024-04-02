from django.contrib import admin
from .models import Smoothie, Categories

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class SmoothieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


admin.site.register(Smoothie, SmoothieAdmin)
admin.site.register(Categories, CategoriesAdmin)