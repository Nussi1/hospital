from django.contrib import admin
from .models import Hospital, MainDoctor, TreatDoctor, Nurse, Patient, Customer, Appointment

admin.site.register(Hospital)
admin.site.register(MainDoctor)
admin.site.register(TreatDoctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Customer)
admin.site.register(Appointment)
