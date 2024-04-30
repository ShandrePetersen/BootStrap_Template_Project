from django.contrib import admin

from .models import ContactMessage

from .forms import ContactForm

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','message')
    search_fields = ('name', 'email', 'phone','message')
