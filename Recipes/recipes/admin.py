from django.contrib import admin

from .models import Recipe,RecipeIngredient
# Register your models here.

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
   # fields = ['name','quantity','unit','directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display=['name','user']
    readonly_fields = ['timestamp','updated']
    raw_id_fields = ['user']

admin.site.register(Recipe,RecipeAdmin)
#admin.site.register(RecipeIngredient)