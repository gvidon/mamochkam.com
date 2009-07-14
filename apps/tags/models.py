from django.db import models

class Tag(models.Model):
	title = models.CharField(max_length=50)
	object_id = models.PositiveIntegerField()
	object_type = models.CharField(max_length=6, choices=(
		('article', 'Article'),
		('photo', 'Photo'),
	))
	
	#META
	class Meta:
		db_table = 'tag'
