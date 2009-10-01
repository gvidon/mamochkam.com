# -*- coding: utf-8 -*-
from datetime                     import datetime
from PIL                          import Image

from django.contrib.auth.models   import User
from django.conf                  import settings
from django.db                    import models

from mamochkam.apps.common.models import Entity

#COMMENTS MODEL
class VideoComment(models.Model):
	user     = models.ForeignKey(User)
	pub_date = models.DateTimeField(auto_now_add=True)
	text     = models.CharField(max_length=255)
	
	#STRING REPRESENTATION
	def __unicode__(self):
		return self.text
	
	class Meta:
		ordering            = ['pub_date',]
		db_table            = 'video_comment'
		verbose_name        = u'Комметарий'
		verbose_name_plural = u'Комментарии'

#MAIN VIDEO MODEL
class Video(models.Model, Entity):
	pub_date = models.DateTimeField(default=datetime.now)
	video    = models.ImageField(upload_to='upload/video')
	thumb    = models.ImageField(upload_to='upload/video')
	title    = models.CharField(max_length=50)
	comments = models.ManyToManyField(VideoComment, blank=True)
	publish  = models.BooleanField('Publish on site', default=False)
	
	#STRING REPRESENTATION
	def __unicode__(self):
		return self.title
	
	#RESIZE THUMB TO 100x100
	def resize_thumb(self):
		image = Image.open(self.thumb.path)
		
		image.thumbnail((100, 100), Image.ANTIALIAS)
		image.save(self.thumb.path, image.format)
	
		return True
	
	#PREPARE URL
	def thumb_url(self):
		try:
			return settings.MEDIA_URL+self.photo.path[len(settings.MEDIA_ROOT)-1:]+'_thumb'
		
		except KeyError:
			return ''
	
	#META
	class Meta:
		db_table            = 'video'
		verbose_name        = u'Видео клип'
		verbose_name_plural = u'Видео клипы'
