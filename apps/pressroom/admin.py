from django.contrib                  import admin
from mamochkam.apps.pressroom.models import ArticleComment, ArticlePhoto, Article, Section

class PhotoInline(admin.TabularInline):
	model   = ArticlePhoto
	fk_name = 'article'

class ArticleCommentAdmin(admin.ModelAdmin):
	pass
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('headline', 'pub_date', 'is_news', 'is_school')
	inlines = [ PhotoInline, ]
	
class SectionAdmin(admin.ModelAdmin):
	pass

admin.site.register(ArticleComment, ArticleCommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)

