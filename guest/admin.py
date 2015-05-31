from django.contrib import admin
from guest.models import Item, Record, Agent, ItemType

# class RecordInline(admin.TabularInline):
# 	model = Record
# 	extra = 1

# class AgentInline(admin.TabularInline):
# 	model = Agent
# 	extra = 1

# class RecordAdmin(admin.ModelAdmin):
# 	fieldsets = [Ite
# 		(None,               {'fields': ['m_text']}),
# 		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
# 	]
# 	inlines = [AgentInline]
# 	inlines = [RecordInline]

admin.site.register(Item)
admin.site.register(Agent)
admin.site.register(Record)
admin.site.register(ItemType)


# Register your models here.
