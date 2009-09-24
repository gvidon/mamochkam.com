# -*- coding: utf-8 -*-
from django                       import forms
from django.forms                 import ModelForm

from mamochkam.apps.photos.models import Gallery
from mamochkam.apps.photos.models import Photo

#FULL PROFILE
class PhotoForm(ModelForm):
	title = forms.CharField(required=True, max_length=50, error_messages={
		'invalid'   : u'Вы использовали запрещенные символы в подписе',
		'max_length': u'Слишком длинная подпись, более 50-ти символов',
		'empty'     : u'Слишком короткая подпись, менее 1-го символа',
		'required'  : u'А где название?',
	})
	
	photo = forms.ImageField(required=True, error_messages={
		'invalid_image': u'Это не картинка!',
		'required'     : u'Нужен файл с изображением',
		'empty'        : u'Пустой файл',
	})
	
	gallery = forms.ModelChoiceField(queryset=Gallery.objects.all(), error_messages={
		'required': u'В какую галлерею добавим изображение?',
	}, empty_label='')
	
	class Meta:
		model = Photo

