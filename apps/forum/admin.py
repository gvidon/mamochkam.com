from django.contrib              import admin
from mamochkam.apps.forum.models import ThreadComment, Thread

class ThreadCommentAdmin(admin.ModelAdmin):
	pass
	
class ThreadAdmin(admin.ModelAdmin):
	pass

admin.site.register(ThreadComment, ThreadCommentAdmin)
admin.site.register(Thread, ThreadAdmin)

