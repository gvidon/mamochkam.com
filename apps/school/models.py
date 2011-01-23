# -*- coding: utf-8 -*-
from django.contrib.auth.models   import User
from django.db                    import models

#FORUM THREAD
class Direction(models.Model):
	created_at  = models.DateTimeField(auto_now_add=True)
	slug        = models.CharField(u'Имя ссылки', help_text=u'латинские буквы, цифры и "-"', max_length=255)
	title       = models.CharField(u'Название', max_length=255)
	announce    = models.TextField(u'Кратко', blank=True, null=True)
	description = models.TextField(u'Описание')
	priority    = models.IntegerField(blank=True, default=0)
	
	#META
	class Meta:
		ordering            = ['priority',]
		verbose_name        = u'Направление школы'
		verbose_name_plural = u'Направления школы'
