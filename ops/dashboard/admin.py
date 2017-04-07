from django.contrib import admin

# Register your models here.

from .models import Store, Employee, Service, Transaction, Customer

admin.site.register(Store)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Transaction)
admin.site.register(Customer)
# admin.site.register(Attendance)
