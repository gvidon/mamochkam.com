from django.db                    import models
from mamochkam.apps.search.models import Tag

#PORTAL ENTITIES BASE CLASS
class Entity():
	#ATTACH TAG TO ENTITY
	def attach_tags(self, tags_string):
		[Tag.objects.create(
			title       = tag.strip(),
			object_id   = self.id,
			object_type = self.__class__.__name__.lower()
		) for tag in set(tags_string.split(',')) if tag.strip()]
		
		return 1
	
