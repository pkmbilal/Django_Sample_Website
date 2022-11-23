from django.contrib import admin
from .models import Services, Portfolio, ContactUs

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'description', 'btn_text', 'image')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

# Register your models here.
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio)
admin.site.register(ContactUs, ContactAdmin)