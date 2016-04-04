from django.contrib import admin
from .models import objetoTest
from .models import send_points
from .models import PointsT

admin.site.register(PointsT)
admin.site.register(objetoTest)
admin.site.register(send_points)
# Register your models here.
