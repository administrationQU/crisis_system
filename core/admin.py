from django.contrib import admin
from .models import Category, Topic, Protocol, Step, Profile

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Protocol)
admin.site.register(Profile)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('protocol', 'step_number')