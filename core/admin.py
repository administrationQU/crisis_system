from django.contrib import admin
from .models import Category, Topic, Protocol, Step

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Protocol)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('protocol', 'step_number')