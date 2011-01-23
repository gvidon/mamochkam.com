# -*- coding: utf-8 -*-
import smtplib

from email.mime.multipart       import MIMEMultipart
from email.mime.text            import MIMEText

from django.conf                import settings
from django.contrib.auth.models import User
from django.db                  import models

#ADDITIONAL USER ATTRIBUTES AND FLAGS
class Profile(models.Model):
	user        = models.ForeignKey(User, verbose_name=u'Системный пользователь', related_name='profiles')
	avatar      = models.ImageField(upload_to='upload/avatars', verbose_name=u'Автар', blank=True, null=True)
	
	auth_type   = models.CharField(max_length=6, choices=(
		('Local' , 'local'),
		('OpenId', 'openid'),
	), verbose_name=u'Способ авторизации', blank=True, default='local')
	
	sur_name    = models.CharField(max_length=64, verbose_name=u'Отчество', blank=True, null=True)
	
	gender      = models.CharField(max_length=6, choices=[
		('male', u'Мужской'), ('female', u'Женский')
	], verbose_name=u'Пол', blank=True, null=True)
	
	birthdate   = models.DateTimeField(verbose_name=u'Дата рождения', blank=True, null=True)
	phone       = models.CharField(max_length=10, verbose_name=u'Телефон', blank=True, null=True)
	icq         = models.CharField(max_length=12, blank=True, null=True)
	
	consults_in = models.CharField(max_length=64, verbose_name=u'Область в которой может консультировать', blank=True, null=True)
	
	def __unicode__(self):
		return (' ').join((self.user.first_name, self.user.last_name,))
	
	#SEND CUSTOM EMAIL FROM SYSTEM TO USER
	def send_email(self, subject, text_part, html_part):
		msg = MIMEMultipart('alternative')
		msg.set_param('charset', 'utf-8')
		
		msg['Subject'] = subject
		msg['From']    = 'do-not-reply@mamochkam.com'
		msg['To']      = self.user.email
		
		msg.attach(MIMEText(text_part, _subtype='plain', _charset = 'utf-8'))
		msg.attach(MIMEText(html_part, _subtype='html' , _charset = 'utf-8'))
		
		s = smtplib.SMTP('localhost')
		s.sendmail(msg['From'], msg['To'], msg.as_string())
		s.quit() 
		
	class Meta:
		app_label = 'auth'
		db_table  = 'profile'

#ACTIVATION VALUES
class Activation(models.Model):
	user          = models.ForeignKey(User)
	
	type          = models.CharField(max_length=5, choices=(('Email', 'email'), ('Phone', 'phone')), default='email')
	value         = models.CharField(max_length=64)
	code          = models.CharField(max_length=64)
	
	request_date  = models.DateTimeField(auto_now_add=True)
	confirm_date  = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table = 'activation'

	
