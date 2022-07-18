from django.contrib import admin

# Register your models here.
from .models import Departments, Doctors, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display= ('p_name','p_phone')
class DepartmentsAdmin(admin.ModelAdmin):
    list_display=('dep_name','dep_decription')
class DoctorsAdmin(admin.ModelAdmin):
    list_display=('doc_name','doc_spec','dep_name','doc_image')

admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Doctors,DoctorsAdmin)
admin.site.register(Booking,BookingAdmin)