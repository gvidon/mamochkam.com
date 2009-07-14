# -*- coding: utf-8 -*-
from django       import forms
from django.forms import ModelForm
from models       import Bulletin

#BULLETIN FORM
class BulletinForm(ModelForm):
	title = forms.CharField(required=True, max_length=70, error_messages={
		'invalid'   : u'Вы использовали запрещенные символы в загаловке объявленя',
		'max_length': u'Слишком длинный заголовок объявления, более 70-ти символов',
		'empty'     : u'Нужен заголовок',
	})
	
	description = forms.CharField(required=True, max_length=255, error_messages={
		'invalid'   : u'Вы использовали запрещенные символы в тексте объявления',
		'max_length': u'Слишком длинная подпись, более 50-ти символов',
		'empty'     : u'А где сам текст объявления?',
	})

	class Meta:
		model = Photo

