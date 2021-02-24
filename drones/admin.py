from django.contrib import admin
from .models import Pilot,Drone,DroneCategory,Competition
# Register your models here.
admin.site.register(Pilot)
admin.site.register(Drone)
admin.site.register(DroneCategory)
admin.site.register(Competition)
