# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers       import reverse
from django.template.context        import RequestContext
from django.core.exceptions         import ValidationError
from django.views.generic           import list_detail
from django.shortcuts               import get_object_or_404, render_to_response
from django.conf                    import settings
from django.http                    import HttpResponseRedirect, HttpResponse, Http404

from models                         import Answer, Question

# ДОБАВЛЕНИЕ ОТВЕТА
def answer(request, id):
	
	question = get_object_or_404(Question, pk=id)
	
	try:
		Answer.objects.create(
			question = question,
			text     = request.POST['text'],
			
			user = (request.user == question.user or request.user.get_profile().consults_in) and request.user or None,
		)
	
	except (ValueError, KeyError):
		pass
	
	return HttpResponseRedirect(reverse('question', kwargs={'id': id}))

# ОТВЕТЫ НА ЗАДАННЫЙ ВОПРОС
def question(request, id):
	question = get_object_or_404(Question, pk=id)
	
	return list_detail.object_list(request,
		queryset      = question.answers.all(),
		allow_empty   = True,
		template_name = 'consults/question.html',
		
		extra_context = {
			'question' : question,
			'is_author': request.user == question.user,
			'is_master': request.user.is_authenticated() and request.user.get_profile().consults_in,
		}
	)

#ДОБАВЛЕНИЕ ВОПРОСА
@login_required
def new_question(request):
	from django.contrib.auth.models import User
	
	error = {}
	
	if request.POST:
		if not request.POST.get('title'):
			error['title'] = u'У вопроса обязательно должна быть тема'
			
		if not request.POST.get('text'):
			error['text'] = u'Нужны подробности'
		
		try:
			if not error:
				Question.objects.create(
					user   = request.user,
					master = get_object_or_404(User, pk=request.POST['master']),
					
					title  = request.POST['title'],
					text   = request.POST['text']
				)
		except KeyError:
			raise Http404
		
	return render_to_response('consults/new-question.html', {
		'masters': User.objects.exclude(profiles__consults_in=None),
		'title'  : request.POST.get('title'),
		'text'   : request.POST.get('text'),
		'error'  : error,
	}, context_instance=RequestContext(request))
