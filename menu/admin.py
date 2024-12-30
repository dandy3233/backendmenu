from django.contrib import admin
from .models import Burger

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price')
    search_fields = ('name', 'type')
    list_filter = ('type',)
