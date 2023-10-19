from django.contrib import admin

# Register your models here.

from . models import Category, Product

# admin.site.register(Catagory)

# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug':('name',)} # declear the name 
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug':('title',)}