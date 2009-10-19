from django.db                    import models
from mamochkam.apps.search.models import Tag

#PORTAL ENTITIES BASE CLASS
class Entity():
	#ATTACH TAG TO ENTITY
	def attach_tags(self, tags_string):
		for tag in filter(lambda t: t.strip(), set(tags_string.split(','))):
			try:
				self.tags.add(Tag.objects.get(title=tag.strip()))
			
			except Tag.DoesNotExist:
				self.tags.create(title=tag.strip())
			
		return 1
	
