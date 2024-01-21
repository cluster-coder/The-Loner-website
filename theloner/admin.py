from django.contrib import admin

# Register your models here.
from .models import choices, SecretUrl, additionalHtml

#admin.site.register(choices)
admin.site.register(SecretUrl)

#from here below will try my own implementation of the admin 
class ChoicesAdmin(admin.ModelAdmin):
	list_display = ['wolfText','position','urlBearer' ]
	list_filter = ['urlBearer']

class pageAdditionalHtml(admin.ModelAdmin):
	list_display= ['__str__','Pages_its_used_in','options_its_used_in','tagClasses']
	list_filter = ['pages_adding_me', 'options_adding_me']

admin.site.register(choices, ChoicesAdmin)
admin.site.register(additionalHtml,pageAdditionalHtml)
