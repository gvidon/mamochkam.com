from datetime                        import datetime

from django.shortcuts                import render_to_response
from django.template.context         import RequestContext
from django.views.generic            import list_detail
from django.http                     import Http404
from django.conf                     import settings

from mamochkam.apps.pressroom.models import Article, Section

def view_section(request, slug, page=1):
	try:
		section  = Section.objects.get(slug__exact=slug)
		articles = section.articles.filter(publish=True, is_news=False)
	
	except Section.DoesNotExist:
		raise Http404
	
	return list_detail.object_list(request,
		queryset      = articles,
		paginate_by   = settings.ITEMS_PER_PAGE,
		page          = page,
		allow_empty   = True,
		template_name = 'pressroom/article_list.html',
		extra_context = { 'section': section, 'type': 'articles', 'url': '/pressroom/articles/' }
	)
