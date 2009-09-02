from django.contrib               import admin
from mamochkam.apps.photos.models import Photo, Gallery

class PhotoAdmin(admin.ModelAdmin):
	pass

class GalleryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)

