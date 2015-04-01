from django.contrib import admin
from guest.models import Item, Record, Agent

class RecordInline(admin.TabularInline):
	model = Record
	extra = 1

class AgentInline(admin.TabularInline):
	model = Agent
	extra = 1

class ItemAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['Item_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [AgentInline]
	inlines = [RecordInline]

admin.site.register(Item,ItemAdmin)
admin.site.register(Agent)


# Register your models here.
