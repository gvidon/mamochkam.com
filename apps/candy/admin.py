from django.contrib import admin
from models         import Category, Product, ProductPhoto

class PhotoInline(admin.TabularInline):
	model   = ProductPhoto
	fk_name = 'product'

class CategoryAdmin(admin.ModelAdmin):
	pass
	
class ProductAdmin(admin.ModelAdmin):
	inlines = [ PhotoInline, ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

