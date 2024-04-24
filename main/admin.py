from django.contrib import admin
from .models import *


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'lname', 'job']
    list_display_links = ['name', 'lname']


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
    list_display_links = ['title']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_display_links = ['title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'lname', 'email', 'message']
    list_display_links = ['name', 'lname', 'email']


@admin.register(ContactInfo)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone1', 'phone1']
    list_display_links = ['address', 'phone1', 'phone1']


@admin.register(HappyClients)
class HappiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'lname', 'message']
    list_display_links = ['name', 'lname']


@admin.register(WorkExp)
class WorkExpAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'address', 'date']
    list_display_links = ['title', 'company']


@admin.register(Education)
class WorkExpAdmin(admin.ModelAdmin):
    list_display = ['title', 'university', 'place']
    list_display_links = ['title', 'university']


@admin.register(Services)
class WorkExpAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_display_links = ['title']
