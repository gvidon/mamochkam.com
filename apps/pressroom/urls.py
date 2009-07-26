from django.conf.urls.defaults    import *
from django.conf                  import settings
from models                       import Article

# just articles 
urlpatterns = patterns('django_apps.pressroom.views',
    url(r'^$', 'index', name="pr-index"),
    url(r'^articles/section/(?P<slug>[\-\d\w]+)/$'                      , 'view_section', name="pr-section"),
    url(r'^articles/section/(?P<slug>[\-\d\w]+)/page/(?P<page>[0-9]+)/$', 'view_section', name="pr-section-page")
)

# articles and news
querysets = {
	'articles': Article.objects.filter(is_news=False, publish=True),
	'news'    : Article.objects.filter(is_news=True, publish=True),
}

for key, queryset in querysets.items():
	args = {
		'date_field'   : 'pub_date',
		'allow_empty'  : True,
		'queryset'     : queryset,
		'extra_context': { 'type': key, 'url': '/pressroom/'+key },
	}
	
	urlpatterns += patterns('django.views.generic.date_based',
		  url(r'^'+key+'/archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', args, name='pr-'+key+'-archive-month'),
		  url(r'^'+key+'/archive/(?P<year>\d{4})/$'                    , 'archive_year' , args, name='pr-'+key+'-archive-year'),
		  url(r'^'+key+'/archive/?$'                                   , 'archive_index', args, name='pr-'+key+'-archive'),
	)
	
	urlpatterns += patterns('django.views.generic.list_detail',
		url(r'^'+key+'/?(page/(?P<page>[0-9]+)/?)?$', 'object_list', {
			'paginate_by'  : settings.ITEMS_PER_PAGE,
			'allow_empty'  : True,
			'queryset'     : queryset,
			'extra_context': { 'type': key, 'url': '/pressroom/'+key },
		}, name='pr-'+key+'-list'),
	)

urlpatterns += patterns('django.views.generic.list_detail', url(r'^(?P<slug>[\-\d\w]+)/$', 'object_detail', {
	'slug_field': 'slug',
	'queryset'  : Article.objects.all()
}, name='pr-'+key+'-detail'))
