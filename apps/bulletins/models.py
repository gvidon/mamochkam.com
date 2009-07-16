from datetime                     import datetime
from django.contrib.auth.models   import User
from django.db                    import models
from mamochkam.apps.portal.models import Entity

class Bulletin(models.Model, Entity):
	user         = models.ForeignKey(User)
	pub_date     = models.DateTimeField(default=datetime.now)
	is_published = models.BooleanField(default=None)
	
	phone        = models.CharField(max_length=15)
	email        = models.EmailField(max_length=40)
	icq          = models.PositiveIntegerField(max_length=40)
	
	title        = models.CharField(max_length=70)
	description  = models.CharField(max_length=255)
