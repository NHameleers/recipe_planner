from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models


from .models import Recipe, Ingredient



# class RecipeAdmin(admin.ModelAdmin):
# 	formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'30'})}, }

admin.site.register(Recipe)
admin.site.register(Ingredient)


