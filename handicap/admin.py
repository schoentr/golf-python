from django.contrib import admin
from .models import Course, Tee, Round

# Register your models here.
admin.site.register(Course)
admin.site.register(Tee)
admin.site.register(Round)