from django.contrib import admin
from .models import User, EmpA, EmpS



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')




# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(EmpA)
admin.site.register(EmpS)
