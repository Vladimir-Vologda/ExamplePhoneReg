from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.forms import CustomUserChangeFormInAdmin, CustomUserRegistrationForm
from users.models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFormInAdmin
    add_form = CustomUserRegistrationForm

    list_display = (
        'name', 'phone', 'full_name', 'birthday', 'avatar',
        'registration_date', 'is_active', 'is_staff', 'slug',
    )
    list_display_links = (
        'name', 'phone', 'slug',
    )
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'avatar', 'birthday', 'slug')}),
        ('Personal info', {'fields': ('name', 'phone')}),
        ('Permission', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('name', 'phone')
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.unregister(Group)
