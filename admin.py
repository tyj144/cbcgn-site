from django.contrib import admin
from content.models import Event, Category, Sermon

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('title',) }

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('title',) }

class EventInline(admin.StackedInline):
	model = Event
	extra = 0
	ordering = ('-start_date',)

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sermon)