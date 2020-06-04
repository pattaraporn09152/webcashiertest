from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', )
    list_select_related = ('profile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class IncustummerAdmin(admin.ModelAdmin):
    model = Incustumer
    list_display=(
        'face_id',
        'first_name',
        'last_name',
             
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)

admin.site.register(Incustumer, IncustummerAdmin)
admin.site.register(Product)

admin.site.register(Employees)




 

