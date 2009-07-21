from datetime import datetime
from PIL      import Image

from django.contrib.auth.models import User
from django.conf                import settings
from django.db                  import models

from mamochkam.apps.portal.models import Entity

#GALLERY MODEL
class Gallery(models.Model):
	title       = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	slug        = models.CharField(max_length=50)
	
	#TEXT REPRESENTATION
	def __str__(self):
		return self.title
	
	#ADMIN
	class Admin:
		prepopulated_fields = {'slug': ('title',)}
	
	#META
	class Meta:
		db_table = 'gallery'

#COMMENTS MODEL
class PhotoComment(models.Model):
	user     = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.now)
	text     = models.CharField(max_length=255)
	
	#META
	class Meta:
		db_table = 'photo_comment'

#MAIN PHOTO MODEL
class Photo(models.Model, Entity):
	#user     = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.now)
	gallery  = models.ForeignKey(Gallery)
	photo    = models.ImageField(upload_to='/home/nide/code/mamochkam/media/upload/photos')
	title    = models.CharField(max_length=50)
	comments = models.ManyToManyField(PhotoComment, blank=True)
	
	#GENERATE PHOTO THUMBNAIL
	def generate_thumb(self, output=None):
		image = Image.open(self.photo.path)
		
		if(not output):
			output = self.photo.path+'_thumb'
		
		if image.mode not in ('L', 'RGB'):
			image = image.convert('RGB')
	
		image.thumbnail((100, 100))
		image.save(output, image.format)
	
		return output
	
	#PREPARE URL
	def url(self):
		try:
			return settings.MEDIA_URL+self.photo.path[len(settings.MEDIA_ROOT)-1:]
		
		except KeyError:
			return ''
	
	#META
	class Meta:
		db_table = 'photo'
