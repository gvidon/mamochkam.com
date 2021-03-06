from django.contrib import admin
from models         import *

class PhotoInline(admin.TabularInline):
	model   = ProductPhoto
	fk_name = 'product'

class CategoryAdmin(admin.ModelAdmin):
	exclude = ('parent',)
	
class OrderAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'city', 'sum')
	
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'quantity', 'sum')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'is_active', 'is_featured')
	inlines = [ PhotoInline, ]

admin.site.register(Category , CategoryAdmin)
admin.site.register(Order    , OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Product  , ProductAdmin)

