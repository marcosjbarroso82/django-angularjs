from django.contrib import admin

from .models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class PollModelAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]



admin.site.register(Poll, PollModelAdmin)