from datetime                     import datetime
from django.contrib.auth.models   import User
from django.db                    import models
from mamochkam.apps.common.models import Entity

class Bulletin(models.Model, Entity):
	user         = models.ForeignKey(User)
	pub_date     = models.DateTimeField(auto_now_add=True)
	publish      = models.BooleanField(default=None)
	
	title        = models.CharField(max_length=70)
	description  = models.CharField(max_length=255)
	
	#META
	class Meta:
		db_table = 'bulletin'
