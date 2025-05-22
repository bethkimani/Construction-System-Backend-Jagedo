from django.contrib import admin
from .models import User, Customer, Fundi, Contractor, Professional, Hardware

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_fundi', 'is_contractor', 'is_professional', 'is_hardware')
    list_filter = ('is_customer', 'is_fundi', 'is_contractor', 'is_professional', 'is_hardware')

admin.site.register(Customer)
admin.site.register(Fundi)
admin.site.register(Contractor)
admin.site.register(Professional)
admin.site.register(Hardware)
