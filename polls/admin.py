from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

admin.site.register(Poll, PollAdmin)
