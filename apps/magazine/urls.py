# -*- coding: utf-8 -*-
import os, re

from datetime                     import datetime
from django.conf                  import settings
from django.conf.urls.defaults    import *

urlpatterns = patterns('django.views.generic.simple',
	url(r'^price/?$', 'direct_to_template', {'template': 'magazine/price.html'}, name='magazine-price'),
	url(r'^oreol/?$', 'direct_to_template', {'template': 'magazine/oreol.html'}, name='magazine-oreol'),
	
	# страница с номерами журнала, номера в листе (номер, размер в килобайтах)
	url(r'^/?$', 'direct_to_template', {'template': 'magazine/volumes.html', 'extra_context': {
		'volumes': sorted([
			
			[entry,
				datetime.strptime(entry, '%m.%Y.pdf'),
				float(os.stat(settings.PDF_ROOT+entry)[6])/1000
			]
			
			for entry in os.listdir(settings.PDF_ROOT)
			
			if not os.path.isdir(settings.PDF_ROOT+entry)
				and re.match(r'^\d{2}\.\d{4}\.pdf$', entry, re.IGNORECASE)
		
		], reverse=True)
	}}, name='magazine-volumes'),
)

