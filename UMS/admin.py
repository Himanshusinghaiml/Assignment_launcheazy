from django.contrib import admin
from .models import Organization, Role, MembershipRequest

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'billing_group']

admin.site.register(Organization, OrganizationAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization']

admin.site.register(Role, RoleAdmin)

class MembershipRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'organization', 'is_accepted']
    list_filter = ['organization', 'is_accepted']

admin.site.register(MembershipRequest, MembershipRequestAdmin)
