from django.contrib import admin
from .models import Category, Topic, Protocol, Step , About , ProjectGoal

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Protocol)
admin.site.register(About)
admin.site.register(ProjectGoal)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('protocol', 'step_number')