# -*- coding: utf-8 -*-
from datetime                     import datetime
from PIL                          import Image

from django.contrib.auth.models   import User
from django.conf                  import settings
from django.db                    import models

from mamochkam.apps.common.models import Entity
from mamochkam.apps.search.models import Tag
from mamochkam.apps.utils         import images

#GALLERY MODEL
class Gallery(models.Model):
	title       = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	slug        = models.CharField(max_length=50)
	
	#STRING REPRESENTATION
	def __unicode__(self):
		return self.title
	
	'''
	#ADMIN
	class Admin:
		prepopulated_fields = {'slug': ('title',)}
	'''
	
	#META
	class Meta:
		db_table            = 'gallery'
		verbose_name        = u'Галлерея'
		verbose_name_plural = u'Галлереи'

#COMMENTS MODEL
class PhotoComment(models.Model):
	user     = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.now)
	text     = models.CharField(max_length=255)
	
	#STRING REPRESENTATION
	def __unicode__(self):
		return self.text
	
	#META
	class Meta:
		ordering            = ['pub_date',]
		db_table            = 'photo_comment'
		verbose_name        = u'Комментарий'
		verbose_name_plural = u'Комментарии'

#MAIN PHOTO MODEL
class Photo(models.Model, Entity):
	user     = models.ForeignKey(User, related_name='photos')
	pub_date = models.DateTimeField(default=datetime.now)
	gallery  = models.ForeignKey(Gallery)
	photo    = models.ImageField(upload_to='upload/photos')
	title    = models.CharField(max_length=50)
	publish  = models.BooleanField('Publish on site', default=False)
	
	comments = models.ManyToManyField(PhotoComment, blank=True)
	tags     = models.ManyToManyField(Tag, related_name='photos', db_table='photo_tag', blank=True)
	
	#STRING REPRESENTATION
	def __unicode__(self):
		return self.title
	
	#СОХРАНИТЬ ФОТО И СОЗДАТЬ THUMB
	def save(self):
		super(Photo, self).save()
		
		images.resize(self.photo.path)
		images.generate_thumb(self.photo.path, (100, 100))
	
	#PREPARE URL
	def thumb_url(self):
		try:
			return self.photo.url+'_thumb'
		
		except KeyError:
			return ''
	
	#META
	class Meta:
		db_table            = 'photo'
		verbose_name        = u'Изображение'
		verbose_name_plural = u'Изображения'
