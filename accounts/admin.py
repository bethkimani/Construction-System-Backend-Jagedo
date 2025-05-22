from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type', 'phone_number', 'profile_picture')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(Skill)
admin.site.register(Fundi)
admin.site.register(Contractor)
admin.site.register(Professional)
admin.site.register(Hardware)
admin.site.register(MaterialCategory)
admin.site.register(Material)
admin.site.register(Project)
admin.site.register(ProjectMaterial)
admin.site.register(Task)
admin.site.register(ChatbotConversation)
admin.site.register(ChatbotMessage)
