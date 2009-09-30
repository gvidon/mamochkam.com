from django.contrib              import admin
from mamochkam.apps.video.models import VideoComment, Video

class VideoCommentAdmin(admin.ModelAdmin):
	pass
	
class VideoAdmin(admin.ModelAdmin):
	pass

admin.site.register(VideoComment, VideoCommentAdmin)
admin.site.register(Video, VideoAdmin)

