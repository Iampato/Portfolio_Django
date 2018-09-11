from django.contrib import admin
from .models import Post,subscriber

class subscriberAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Email', 'sent_on')
	list_filter = ( 'active','sent_on', 'updated')
	search_fields = ('Name', 'Email')
admin.site.register(subscriber, subscriberAdmin)
