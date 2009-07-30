# -*- coding: utf-8 -*-
from datetime import datetime

from django.conf             import settings
from django.template.context import RequestContext
from django.views.generic    import list_detail
from django.shortcuts        import render_to_response
from django.http             import HttpResponse, Http404

from models import Gallery
from forms  import PhotoForm

#GALLERY'S PHOTOS LIST
def photos(request, slug, page=1):
	try:
		gallery = Gallery.objects.get(slug__exact=slug)
		photos = gallery.photos.all()
	
	except Gallery.DoesNotExist:
		raise Http404
	
	return list_detail.object_list(request,
		queryset      = photos,
		paginate_by   = settings.ITEMS_PER_PAGE,
		page          = page,
		allow_empty   = True,
		template_name = 'photos/photo_list.html',
		extra_context = { 'gallery': gallery }
	)

#UPLOAD USER'S PHOTO
#**WARN** @login_required
def upload(request):
	form = PhotoForm()
	
	if(request.POST):
		form = PhotoForm({
			#'user'    : 1,
			'pub_date': datetime.now(),
			'gallery' : request.POST['gallery'],
			'title'   : request.POST['title'],
		}, request.FILES)
		
		if(form.is_valid()):
			model = form.save()
			
			model.attach_tags(request.POST['tags'])
			model.generate_thumb()
			
			return render_to_response(
				'photos/uploaded.html',
				{ 'img_src': model.url() },
				context_instance=RequestContext
			)
	
	return render_to_response(
		'photos/upload.html',
		{'form': form,},
		context_instance=RequestContext(request)
	)
