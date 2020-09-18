from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.site_header = 'Cloudini Administration Panel'

UserAdmin.list_display = ('username', 'organization', 'email', 'date_joined', 'is_active', 'is_staff', 'isAdmin')

class OrganizationDisplay(admin.ModelAdmin):
    list_display = ('name', 'scan_status', 'last_scan_time')
    list_filter = ('name', 'scan_status', 'last_scan_time')

class PolicyDisplay(admin.ModelAdmin):
    list_display = ('name', 'affectedResources', 'description')
    list_filter = ('name', 'affectedResources', 'description')

class ActivatedPolicyDisplay(admin.ModelAdmin):
    list_display = ('organization', 'policy', 'metadata', 'actionItem')
    list_filter = ('organization', 'policy', 'actionItem')

class ViolationDisplay(admin.ModelAdmin):
    list_display = ('connectedPolicy', 'resource_id', 'isChecked', 'isFixed')
    list_filter = ('connectedPolicy', 'resource_id')

admin.site.register(CloudiniUser, UserAdmin)
admin.site.register(Organization, OrganizationDisplay)
admin.site.register(Policy, PolicyDisplay)
admin.site.register(ActivatedPolicy, ActivatedPolicyDisplay)
admin.site.register(Violation, ViolationDisplay)

#admin.site.unregister(Group)