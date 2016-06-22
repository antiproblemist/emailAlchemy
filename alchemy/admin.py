from django.contrib import admin
from alchemy.models import *

# Register your models here.
class SpamKeywordResource(admin.ModelAdmin):

	class Meta:
		model = spamwords
		fields = ('spamkeywords')
		
admin.site.register(spamwords,SpamKeywordResource)		
		
class SpamAddressResource(admin.ModelAdmin):

	list_display = ['emailAddress', 'ipAddress', 'score', 'notSpamVotes', 'emailHash']
	class Meta:
		model = spamAddress
		
		fields = ('emailAddress', 'ipAddress', 'score', 'notSpamVotes', 'addedByUser')

admin.site.register(spamAddress,SpamAddressResource)
