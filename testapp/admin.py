from django.contrib import admin

from testapp.models import Warden , Customer, Room

# Register your models here.

class WardenAdmin(admin.ModelAdmin):
    list_display=['Name','Address','Phone_No','Emailid']

admin.site.register(Warden,WardenAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['Name','Address','Phone_No','Emailid','room_no','rent','date']

admin.site.register(Customer,CustomerAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display=['room_no','rent']

admin.site.register(Room,RoomAdmin)
