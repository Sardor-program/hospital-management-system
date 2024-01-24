from django.contrib import admin
from hospital.models import Doctor, Patient, Appointment


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'special']


class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'gender', 'address']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'date', 'time']


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
