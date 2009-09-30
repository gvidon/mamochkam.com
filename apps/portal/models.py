from django.db import models

#BANNER DESCRIPTION
class Banner(models.Model):
	image        = models.ImageField(upload_to='upload/banners')
	size         = models.CharField(max_length=16)
	
	counter      = models.IntegerField(blank=True, default=0)
	limit        = models.IntegerField(blank=True, null=True)
	date_limit   = models.DateTimeField(blank=True, null=True)
	
	is_active    = models.BooleanField(blank=True, null=True)
	is_permanent = models.BooleanField(blank=True, null=True)
	
	#META
	class Meta:
		db_table   = 'banner'

#BANNER VIEW LOG
class BannerLog(models.Model):
	banner     = models.ForeignKey(Banner, related_name='log')
	created_at = models.DateTimeField(auto_now_add=True)
	ip         = models.IPAddressField()
	
	#META
	class Meta:
		ordering = ['-created_at',]
		db_table = 'banner_log'
