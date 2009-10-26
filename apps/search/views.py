# -*- coding: utf-8 -*-
from django.contrib.auth.decorators  import login_required
from django.conf                     import settings
from django.template.context         import RequestContext
from django.shortcuts                import render_to_response
from django.http                     import HttpResponse, Http404

from mamochkam.apps.pressroom.models import Article
from mamochkam.apps.forum.models     import Thread
from mamochkam.apps.photos.models    import Photo
from mamochkam.apps.video.models     import Video
from models                          import Tag

type2list = {
	'article': [Article.objects.filter(publish=True), 'pressroom/article_list.html'],
	'photo'  : [Photo.objects.filter(publish=True)  , 'photos/photo_list.html'],
	'video'  : [Video.objects.filter(publish=True)  , 'video/video_list.html'],
	'forum'  : [Thread.objects                      , 'forum/thread_list.html'],
}

#ПОИСК ПО БАЗЕ ТЭГОВ
def by_tag(request, tag, object_type):
	return render_to_response(type2list[object_type][1], {
		'tag'        : tag,
		'object_list': type2list[object_type][0].filter(tags__title=tag)
	}, context_instance=RequestContext(request))
