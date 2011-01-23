from django.contrib.auth.models  import User
from django.contrib              import admin
from mamochkam.apps.users.models import Profile
from models                      import Answer, Question

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('text',)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text',)

class ProfileAdmin(admin.ModelAdmin):
	fields = ('user', 'sur_name', 'gender', 'birthdate', 'consults_in', 'phone', 'icq')

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Profile, ProfileAdmin)

