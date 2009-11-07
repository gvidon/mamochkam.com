from django.conf.urls.defaults import *
from django.conf               import settings
from models                    import Article

# Section urls
urlpatterns = patterns('mamochkam.apps.pressroom.views',
    url(r'^articles/section/(?P<slug>[\-\d\w]+)/$'                      , 'view_section', name="pr-section"),
    url(r'^articles/section/(?P<slug>[\-\d\w]+)/page/(?P<page>[0-9]+)/$', 'view_section', name="pr-section-page")
)

# Articles and news querysets
querysets = {
	'articles': Article.objects.filter(is_news=False, publish=True, is_school=False),
	'news'    : Article.objects.filter(is_news=True, publish=True),
	'school'  : Article.objects.filter(is_news=True, publish=True, is_school=True),
}

for key, queryset in querysets.items():
	
	# Archive list
	urlpatterns += patterns('django.views.generic.date_based',
		url(r'^'+key+'/archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', {
			'date_field'   : 'pub_date',
			'allow_empty'  : True,
			'queryset'     : queryset,
			'template_name': 'pressroom/article_list.html',
			'extra_context': { 'type': key, 'url': '/pressroom/'+key },
		}, name='pr-'+key+'-archive-month'),
	)
	
	# Paginate list
	urlpatterns += patterns('django.views.generic.list_detail',
		url(r'^'+key+'/?(page/(?P<page>[0-9]+)/?)?$', 'object_list', {
			'paginate_by'  : settings.ITEMS_PER_PAGE,
			'allow_empty'  : True,
			'queryset'     : queryset,
			'extra_context': { 'type': key, 'url': '/pressroom/'+key },
		}, name='pr-'+key+'-list'),
	)

# Article details
urlpatterns += patterns('django.views.generic.list_detail', url(r'^(?P<slug>[\-\d\w]+)/$', 'object_detail', {
	'slug_field'   : 'slug',
	'queryset'     : Article.objects.all(),
	'extra_context': { 'type': key, 'url': '/pressroom/'+key },
}, name='pr-'+key+'-detail'))
