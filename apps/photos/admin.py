from django.contrib               import admin
from mamochkam.apps.photos.models import PhotoComment, Photo, Gallery

class PhotoCommentAdmin(admin.ModelAdmin):
	pass
	
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'publish')

class GalleryAdmin(admin.ModelAdmin):
	pass

admin.site.register(PhotoComment, PhotoCommentAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)

