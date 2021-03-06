# -*- coding: utf-8 -*-
from datetime                       import datetime

from django.contrib.auth.decorators import login_required
from django.conf                    import settings
from django.template.context        import RequestContext
from django.views.generic           import list_detail
from django.shortcuts               import render_to_response
from django.http                    import HttpResponse, Http404

from models                         import Gallery, Photo
from forms                          import PhotoForm

#DISPLAY GALLERY'S PHOTOS
def view_gallery(request, slug, page=1):
	try:
		gallery = Gallery.objects.get(slug__exact=slug)
		photos  = Photo.objects.filter(gallery=gallery, publish=True).order_by('-id')
	
	except Gallery.DoesNotExist:
		raise Http404
	
	return list_detail.object_list(request,
		queryset      = photos,
		paginate_by   = settings.ITEMS_PER_PAGE,
		page          = page,
		allow_empty   = True,
		template_name = 'photos/photo_list.html',
		extra_context = { 'gallery': gallery,'url': '/photos/' }
	)

#UPLOAD USER'S PHOTO
@login_required
def upload(request):
	form = PhotoForm(auto_id='%s')
	
	if(request.POST):
		form = PhotoForm({
			'user'    : request.user.id,
			'pub_date': datetime.now(),
			'gallery' : request.POST['gallery'],
			'title'   : request.POST['title'],
		}, request.FILES)
		
		if(form.is_valid()):
			photo = form.save()
			photo.attach_tags(request.POST['tags'])
			
	return render_to_response(
		'photos/upload.html',
		{'form': form,},
		context_instance=RequestContext(request)
	)
