# -*- coding: utf-8 -*-
from django.db import models

#BANNER DESCRIPTION
class Banner(models.Model):
	image        = models.ImageField(u'Изображение баннер', upload_to='upload/banners')
	
	size         = models.CharField(u'Положение на сайте', max_length=16, choices=(
		('160x600', u'Слева'),
		('468x120', u'Сверху'),
		('240x120', u'Справа'),
	))
	
	counter      = models.IntegerField(u'Счетчик посещений', blank=True, default=0)
	limit        = models.IntegerField(u'Лимит показов', blank=True, null=True)
	date_limit   = models.DateTimeField(u'Показывать до даты', blank=True, null=True)
	
	is_active    = models.BooleanField(u'Включен', blank=True, null=True)
	is_permanent = models.BooleanField(u'Постоянно занимает место до истечения показов', blank=True, null=True)
	
	#СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ БАННЕРА
	def __unicode__(self):
		return self.image.url
	
	#META
	class Meta:
		db_table            = 'banner'
		verbose_name        = u'Баннер'
		verbose_name_plural = u'Баннеры'

#BANNER VIEW LOG
class BannerLog(models.Model):
	banner     = models.ForeignKey(Banner, related_name='log')
	created_at = models.DateTimeField(auto_now_add=True)
	ip         = models.IPAddressField()
	
	#META
	class Meta:
		ordering            = ['-created_at',]
		db_table            = 'banner_log'
		verbose_name        = u'Запись'
		verbose_name_plural = u'Отчеты по баннерам'
