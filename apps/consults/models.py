# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db                  import models

#ОТВЕТЫ СПЕЦИАЛИСТОВ
class Answer(models.Model):
	question   = models.ForeignKey('Question', verbose_name=u'Вопрос', related_name='answers')
	user       = models.ForeignKey(User, verbose_name=u'Пользователь', related_name='answers')
	created_at = models.DateTimeField(verbose_name=u'Дата', auto_now_add=True)
	text       = models.TextField(max_length=1024, verbose_name=u'Ответы')
	
	def __unicode__(self):
		return self.text
	
	class Meta:
		verbose_name_plural = u'Ответы'
		verbose_name        = u'Ответ'
		db_table            = 'answer'

#ВОПРОС СПЕЦИАЛИСТУ
class Question(models.Model):
	user       = models.ForeignKey(User, verbose_name=u'Автор вопроса', related_name='question')
	master     = models.ForeignKey(User, verbose_name=u'Кто отвечает?', related_name='questions')
	
	created_at = models.DateTimeField(verbose_name=u'Дата', auto_now_add=True)
	
	title      = models.CharField(max_length=128, verbose_name=u'Заглавие воспроса')
	text       = models.TextField(max_length=1024, verbose_name=u'Подробно')
	
	def __unicode__(self):
		return self.text
	
	class Meta:
		verbose_name_plural = u'Вопросы'
		verbose_name        = u'Вопрос'
		db_table            = 'question'

