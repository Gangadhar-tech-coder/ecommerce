from django.contrib import admin
from .models import Profile,Address
class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile,ProfileAdmin)
class AddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Address,AddressAdmin)
# Register your models here.
