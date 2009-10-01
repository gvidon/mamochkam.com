# -*- coding: utf-8 -*-
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
	
	#STRING REPRESENTATION OF BULLETIN
	def __unicode__(self):
		return self.title
	
	#META
	class Meta:
		db_table            = 'bulletin'
		verbose_name        = u'Объявление'
		verbose_name_plural = u'Объявления'
