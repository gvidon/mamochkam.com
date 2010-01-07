# -*- coding: utf-8 -*-
from datetime                     import datetime

from django.contrib.auth.models   import User
from django.db                    import models
from django.conf                  import settings
from django.core.urlresolvers     import reverse

from mamochkam.apps.common.models import Entity
from mamochkam.apps.search.models import Tag
from mamochkam.apps.utils         import images

'''
# Get relative media path
try:
	PRESSROOM_DIR = settings.PRESSROOM_DIR
except:
	PRESSROOM_DIR = 'pressroom'

# define the models
class ArticleManager(models.Manager):
	def get_published(self):
		return self.filter(publish=True, pub_date__lte=datetime.now)
	
	def get_drafts(self):
		return self.filter(publish=False)
'''

class ArticleComment(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	user     = models.ForeignKey(User)
	text     = models.TextField()
	
	#СТРОКВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.text
	
	#META
	class Meta:
		ordering            = ['pub_date',]
		db_table            = 'article_comment'
		verbose_name        = u'Комментарий'
		verbose_name_plural = u'Комментарии'

#ФОТОГРАФИИ СТАТЬИ
class ArticlePhoto(models.Model):
	article = models.ForeignKey('Article', related_name='photos')
	photo   = models.ImageField(upload_to='upload/photos')
	
	#СОХРАНИТЬ ФОТО И СОЗДАТЬ THUMB
	def save(self):
		super(ArticlePhoto, self).save()
		
		images.resize(self.photo.path)
		images.generate_thumb(self.photo.path, (150, 150))
	
	#ССЫЛКА НА ТУМБ
	def thumb_url(self):
		return self.photo.url+'_thumb'
	
	#СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.photo.path
	
	#META
	class Meta:
		db_table            = 'article_photo'
		verbose_name        = u'Фото для статьи'
		verbose_name_plural = u'Фотографии статьи'

class Article(models.Model, Entity):
	is_news   = models.BooleanField(default=False)
	is_school = models.BooleanField(default=False)
	
	pub_date  = models.DateTimeField('Publish date', default=datetime.now)
	headline  = models.CharField(max_length=200)
	slug      = models.SlugField(help_text='A "Slug" is a unique URL-friendly title for an object.')
	summary   = models.TextField(help_text="A single paragraph summary or preview of the article.")
	body      = models.TextField('Body text')
	
	author    = models.CharField(max_length=255, blank=True, null=True)
	source    = models.CharField(max_length=128, blank=True, null=True)
	
	comments  = models.ManyToManyField(ArticleComment, blank=True)
	tags      = models.ManyToManyField(Tag, related_name='articles', db_table='article_tag', blank=True)
	
	publish   = models.BooleanField(
		u'Опубликовать статью',
		default   = True,
		help_text = u'Статья не появится на сайте пока н опубликована'
	)
	
	sections  = models.ManyToManyField('Section', related_name='articles', blank=True, null=True)
	
	# Custom article manager
	# objects = ArticleManager()
	
	#СТРОКВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.headline
	
	#ССЫЛКА НА СТАТЬЮ
	def get_absolute_url(self):
		args = self.pub_date.strftime("%Y/%b/%d").lower().split("/") + [self.slug]
		return reverse('pr-article-detail', args=args)
	
	#ССЫЛКА НА ТУМБ
	def thumb_url(self):
		try:
			return self.photos.all()[0].thumb_url()
		
		except IndexError:
			return None
	
	class Meta:
		db_table            = 'article'
		ordering            = ['-pub_date']
		get_latest_by       = 'pub_date'
		verbose_name        = u'Статья'
		verbose_name_plural = u'Статьи'

class Section(models.Model):
	title = models.CharField(max_length=80, unique=True)
	slug = models.SlugField()
	
	#СТРОКВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('pr-section', args=[self.slug])

	class Meta:
		db_table            = 'article_section'
		ordering            = ['title']
		verbose_name        = u'Раздел'
		verbose_name_plural = u'Разделы'
	
