# -*- coding: utf-8 -*-
from django.contrib.auth.models   import User
from django.db                    import models
from mamochkam.apps.common.models import Entity

#THREAD COMMENTS
class ThreadComment(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	user     = models.ForeignKey(User)
	text     = models.TextField()
	
	#META
	class Meta:
		db_table = 'thread_comment'

#FORUM THREAD
class Thread(models.Model, Entity):
	user        = models.ForeignKey(User)
	created_at  = models.DateTimeField(auto_now_add=True)
	title       = models.CharField(max_length=128)
	description = models.TextField()
	comments    = models.ManyToManyField(ThreadComment)
	
	#LAST THREAD COMMENT
	def last_comment(self):
		try:
			return self.comments.order_by('-pub_date')[0]
		
		except IndexError:
			return {}
		
	#META
	class Meta:
		db_table = 'thread'
