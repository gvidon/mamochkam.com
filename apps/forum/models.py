# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db                  import models

#THREAD COMMENTS
class ThreadComment(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	author     = models.ForeignKey(User)
	text       = models.TextField()
	
	#META
	class Meta:
		db_table = 'thread_comment'

#FORUM THREAD
class Thread(models.Model):
	author      = models.ForeignKey(User)
	created_at  = models.DateTimeField(auto_now_add=True)
	title       = models.CharField(max_length=128)
	description = models.TextField()
	comments    = models.ManyToManyField(ThreadComment)
	
	#LAST THREAD COMMENT
	def last_comment(self):
		try:
			return self.comments.order_by('-created_at')[0]
		
		except IndexError:
			return {}
		
	#META
	class Meta:
		db_table = 'thread'
