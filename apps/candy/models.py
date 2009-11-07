# -*- coding: utf-8 -*-
from django.db                    import models
from django.contrib.auth.models   import User

from mamochkam.apps.utils         import images
from mamochkam.apps.search.models import Tag

#ВЛОЖЕННЫЕ КАТГЕОРИИ
class Category(models.Model):
	parent      = models.ForeignKey('self', blank=True, null=True)
	
	slug        = models.CharField(max_length='64')
	title       = models.CharField(max_length='64')
	description = models.CharField(max_length='128')
	
	#СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.title
	
	#META
	class Meta:
		db_table            = 'category'
		verbose_name        = u'Категория продуктов'
		verbose_name_plural = u'Категории продуктов'

#ОПИСАНИЕ ЗАКАЗА
class Order(models.Model):
	user         = models.ForeignKey(User)
	
	email        = models.EmailField()
	first_name   = models.CharField(max_length=32, blank=True, null=True)
	last_name    = models.CharField(max_length=32, blank=True, null=True)
	contacts     = models.CharField(max_length=128)
	address      = models.CharField(max_length=255)
	
	is_cancelled = models.BooleanField(default=True)
	is_paid      = models.BooleanField(default=False)
	
	payment_type = models.CharField(max_length=32, choices=(
		(u'Наличные'     , 'cash'),
		(u'WebMoney'     , 'webmoney'),
		(u'Яндекс.деньги', 'yandex'),
	))
	
	sum          = models.FloatField()
	
	#META
	class Meta:
		db_table            = 'order'
		verbose_name        = u'Заказ'
		verbose_name_plural = u'Заказы'

#ПОЗИЦИИ ЗАКАЗА
class OrderItem(models.Model):
	order   = models.ForeignKey(Order)
	product = models.ForeignKey('Product')
	
	title   = models.CharField(max_length='64')
	comment = models.CharField(max_length='128', blank=True, null=True)
	sum     = models.FloatField()
	
	#META
	class Meta:
		db_table            = 'order_item'
		verbose_name        = u'Позиция'
		verbose_name_plural = u'Позиции заказа'

#ПРОДУКТ С ЦЕНОЙ ОПИСАНИЕМ И ГАБАРИТАМИ
class Product(models.Model):
	author      = models.ForeignKey(User, verbose_name=u'Автор изделия', blank=True, null=True)
	category    = models.ManyToManyField('Category', verbose_name=u'Категория', db_table='category_product_ref', related_name='products')
	
	created_at  = models.DateTimeField(auto_now_add=True)
	
	is_active   = models.BooleanField(u'Показывать в магазине', default=True)
	is_featured = models.BooleanField(u'Рекомендуемый товар', default=False)
	
	slug        = models.CharField(u'Имя ссылки для продукта', help_text='латиница, цифры и "-"', max_length='64')
	title       = models.CharField(u'Название', max_length='64')
	description = models.TextField(u'Описание', blank=True, null=True)
	tags        = models.ManyToManyField(Tag, related_name='products', db_table='product_tag', blank=True, null=True)
	
	size        = models.CharField(u'Размеры', help_text='в произвольной форме', max_length='64', blank=True, null=True)
	madeof      = models.CharField(u'Материал', max_length='64', blank=True, null=True)
	price       = models.FloatField(u'Цена')
	
	tags        = models.ManyToManyField(Tag, verbose_name='тэги', related_name='products', db_table='product_tag', blank=True)
	
	#ССЫЛКА НА ТУМБ
	def thumb_url(self):
		try:
			return self.photos.all()[0].thumb_url()
		
		except IndexError:
			return 'default-candy-thumb'
		
	#СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.title
	
	#META
	class Meta:
		db_table            = 'product'
		verbose_name        = u'Продукт магазина'
		verbose_name_plural = u'Продукты'

#ФОТОГРАФИИ ПРОДУКТА
class ProductPhoto(models.Model):
	product = models.ForeignKey(Product, related_name='photos')
	photo   = models.ImageField(upload_to='upload/products')
	
	#СОХРАНИТЬ ФОТО И СОЗДАТЬ THUMB
	def save(self):
		super(ProductPhoto, self).save()
		
		images.resize(self.photo.path)
		images.generate_thumb(self.photo.path, (150, 150))
	
	#ССЫЛКА НА ТУМБ
	def thumb_url(self):
		return self.photo.url+'_thumb'
	
	#СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ
	def __unicode__(self):
		return self.photo.path
	
	#META
	class Meta:
		db_table            = 'product_photo'
		verbose_name        = u'Фото продукта'
		verbose_name_plural = u'Фотографии продукта'

#РЕЙТИНГ НА МАНЕР НРАВИТСЯ/НЕ НРАВИТСЯ
class Vote(models.Model):
	user       = models.ForeignKey(User, blank=True, null=True)
	product    = models.ForeignKey(Product)
	created_at = models.DateTimeField(auto_now_add=True)
	ip         = models.IPAddressField()
	
	#META
	class Meta:
		db_table            = 'vote'
		verbose_name        = u'Голос'
		verbose_name_plural = u'Голоса'
