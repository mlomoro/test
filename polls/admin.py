from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
	inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)

