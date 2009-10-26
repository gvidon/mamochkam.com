# -*- coding: utf-8 -*-
from django.contrib.auth.models   import User
from django.db                    import models

#FORUM THREAD
class Direction(models.Model):
	created_at  = models.DateTimeField(auto_now_add=True)
	slug        = models.CharField(max_length=255)
	title       = models.CharField(max_length=255)
	description = models.TextField()
	priority    = models.IntegerField(blank=True, default=0)
	
	#META
	class Meta:
		ordering            = ['priority',]
		verbose_name        = u'Направление школы'
		verbose_name_plural = u'Направления школы'
