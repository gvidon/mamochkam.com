from datetime import datetime

from django.contrib.auth.models import User
from django.db                  import models
from django.conf                import settings
from django.core.urlresolvers   import reverse

from mamochkam.apps.common.models import Entity

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
	created_at = models.DateTimeField(auto_now_add=True)
	user       = models.ForeignKey(User)
	text       = models.TextField()
	
	#META
	class Meta:
		db_table = 'article_comment'

class Article(models.Model, Entity):
	is_news  = models.BooleanField(default=False)
	pub_date = models.DateTimeField('Publish date', default=datetime.now)
	headline = models.CharField(max_length=200)
	slug     = models.SlugField(help_text='A "Slug" is a unique URL-friendly title for an object.')
	summary  = models.TextField(help_text="A single paragraph summary or preview of the article.")
	body     = models.TextField('Body text')
	author   = models.CharField(max_length=100)
	comments = models.ManyToManyField(ArticleComment)
	
	publish = models.BooleanField(
		'Publish on site',
		default   = True,
		help_text = 'Articles will not appear on the site until their "publish date".'
	)
	
	sections = models.ManyToManyField('Section', related_name='articles')
	
	# Custom article manager
	# objects = ArticleManager()
	
	class Meta:
		db_table      = 'article'
		ordering      = ['-pub_date']
		get_latest_by = 'pub_date'
	
	class Admin:
		prepopulated_fields = { 'slug': ("headline",)}
		list_display        = ('headline', 'author', 'pub_date', 'publish')
		list_filter         = ['pub_date']
		save_as             = True
	
	def __unicode__(self):
		return self.headline
	
	def get_absolute_url(self):
		args = self.pub_date.strftime("%Y/%b/%d").lower().split("/") + [self.slug]
		return reverse('pr-article-detail', args=args)

class Section(models.Model):
	title = models.CharField(max_length=80, unique=True)
	slug = models.SlugField()

	class Meta:
		db_table = 'article_section'
		ordering = ['title']

	class Admin:
		prepopulated_fields = {"slug": ("title",)}
		list_display = ('title',)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('pr-section', args=[self.slug])
	
