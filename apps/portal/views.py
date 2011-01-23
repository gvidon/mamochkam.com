# -*- coding: utf-8 -*-
import json
import datetime

from django.shortcuts                import render_to_response
from django.shortcuts                import get_object_or_404
from django.template                 import RequestContext
from django.http                     import HttpResponseRedirect

from mamochkam.apps.pressroom.models import Article
from models                          import Banner

#РЕДИРЕКТ С БАННЕРА
def advert_redirect(request, banner_id):
	banner = get_object_or_404(Banner, pk=banner_id)
	
	banner.hits = int(banner.hits or 0) + 1
	banner.save()
	
	return HttpResponseRedirect(banner.url)

#PORTAL MAIN PAGE
def index(request):
	try:
		return render_to_response('portal/index.html', {
			'slogans': [
				u'''- Ваш ребенок не говорит? Да вы просто счастливица - он не будет пересказывать
				ваши слова! (Нинон де Ланкло)''',
				
				u'''Будь правдив даже по отношению к дитяти: исполняй обещание, иначе приучишь его
				ко лжи. (Лев Николаевич Толстой)''',
				
				
				u'''Было время, когда  от детей не ожидали ничего, кроме  послушания; теперь от них
				ожидают всего, кроме послушания. (Анатоль Бройяр)''',
				
				u'''Быть правдивыми и честными с детьми, не скрывая от них того, что происходит в
				душе, есть единственное воспитание. (Лев Николаевич Толстой)''',
				
				u'''В воспитании детей главное, чтобы они этого не замечали.<br/>
				Ведь даже люди, которые дарят нашему ребенку  в день рождения барабан и дудку, имели
				бы право на оправдательное слово и на последнее желание
				после него. (В.Нюхтилин, "Мелхиседек", глава "Смерть")''',
				
				u'''Величайшая ошибка, которую обыкновенно делают в воспитании, - не приучат юношество
				к самостоятельному размышлению. (Готхолъд Эфраим Лессинг)''',
				
				u'''Во всяком возрасте почитай родителей. (Екатерина II)''',
				
				u'''Воспитание - это наука, научающая наших детей обходиться без нас. (Эрнст Легуве)''',
				
				u'''Воспитание детей - рискованное дело. Ибо в случае удачи последняя приобретена ценою
				большого труда и заботы, в случае же неудачи горе несравнимо ни с каким другим. (Демокрит)''',
				
				u'''Воспитание детей есть только самосовершенствование, которому ничто не помогает столько, как
				дети. (Лев Николаевич Толстой)''',
				
				u'''Воспитание есть воздействие на сердце тех, кого мы воспитываем. (Лев Николаевич Толстой)''',
				
				u'''Воспитание есть усвоение хороших привычек. (Платон) ''',
			],
			
			'news': Article.objects.filter(is_news=True).order_by('-pub_date'),
		}, context_instance = RequestContext(request))
	
	except Article.DoesNotExist:
		return render_to_response('portal/index.html', {
			'news': [],
		}, context_instance = RequestContext(request))
