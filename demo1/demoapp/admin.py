from django.contrib import admin

from .models import Hotels
from .models import roomtype
from .models import check_availability



# Register your models here.
admin.site.register(Hotels)
admin.site.register(roomtype)
admin.site.register(check_availability)
