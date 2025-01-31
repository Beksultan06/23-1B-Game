from django.contrib import admin
from app.settings.models import Banner, Settings, Contact, ContactFrom
# Register your models here.

@admin.register(Banner)
class bannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'title2']
    list_filter = ['id', 'title', 'title2']
    search_fields = ['id', 'title', 'title2']

admin.site.register(Settings)
admin.site.register(Contact)

@admin.register(ContactFrom)
class ContactFromAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_editable = ['is_active']
    search_fields = ['id', 'name', 'is_active']