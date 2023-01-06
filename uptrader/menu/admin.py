from django.contrib import admin
from django.contrib.auth.models import User
from menu.models import MenuItem, Menu


u = User.objects.get(username='john')
u.set_password('new password')
u.save()





@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_visible', 'order')
    list_editable = ('is_visible', 'order')
    list_filter = ('parent',)


admin.site.register(Menu)
