from django.conf.urls.defaults import *
from django_apps.pressroom.models import *

# custom views
urlpatterns = patterns('django_apps.pressroom.views',
    url(r'^$', 'index', name="pr-index"),
    url(r'^section/(?P<slug>[\-\d\w]+)/$', 'view_section', name="pr-section"),
    url(r'^section/(?P<slug>[\-\d\w]+)/page/(?P<page>[0-9]+)/$', 'view_section', name="pr-section-page")
)

# articlesand news
querysets = {
	'articles': Article.objects.get_published(),
	'news': Article.objects.filter(is_news=True).get_published(),
}

for key, queryset in querysets.items():
	args = {'date_field': 'pub_date', 'allow_empty': True, 'queryset': queryset}
	
	urlpatterns += patterns('django.views.generic.date_based',
		  url(r'^'+key+'/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$', 'object_detail', {'date_field': 'pub_date', 'slug_field': 'slug', 'queryset': Article.objects.all()}, name='pr-'+key+'-detail'),
		  url(r'^'+key+'/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day', args, name='pr-'+key+'-archive-day'),
		  url(r'^'+key+'/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', args, name='pr-'+key+'-archive-month'),
		  url(r'^'+key+'/(?P<year>\d{4})/$', 'archive_year', args, name='pr-'+key+'-archive-year'),
		  url(r'^'+key+'/$', 'archive_index', args, name='pr-'+key+'-archive'),
	)
	
	urlpatterns += patterns('django.views.generic.list_detail',
		  url(r'^'+key+'/page/(?P<page>[0-9]+)/$', 'object_list', {'queryset': queryset, 'allow_empty': True, 'paginate_by': 5}, name='pr-'+key+'-list'),
	)
