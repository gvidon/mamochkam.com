from django.contrib                  import admin
from mamochkam.apps.bulletins.models import Bulletin

class BulletinAdmin(admin.ModelAdmin):
	pass

admin.site.register(Bulletin, BulletinAdmin)

