from django.contrib import admin
from .models import contact_details

# Register your models here.
class contact_detailsAdmin(admin.ModelAdmin):
    list_display = ['Name','Number','Address','email']
admin.site.register(contact_details,contact_detailsAdmin)