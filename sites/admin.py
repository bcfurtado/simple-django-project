from django.contrib import admin

from .models import Site, SiteEntry


class SiteEntryInline(admin.TabularInline):
    model = SiteEntry


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    inlines = [
        SiteEntryInline
    ]
