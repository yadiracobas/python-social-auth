# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserForm, UserChangeForm

#To decode
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserForm
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_admin', 'first_name', 'last_name')
    fieldsets = (
        ('Datos Personales', {'fields': ('first_name', 
        								'last_name',
        								'last_mom_name',
        								'date_of_birth',
        								'gender',
        								 )
       						}
       	),
        ('Datos de contacto', {'fields': (	'email',
        								  	'mobile_no',
        									'avatar'
        									)
        						}
        ),
        ('Permisos', {'fields': ('is_admin', 'is_active', 'is_superuser',
                                'groups', 'user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name', 'first_name', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

