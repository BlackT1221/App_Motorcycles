from django.contrib import admin
from .models import Bike

class BikeAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "trademark",
        "model",
        "price",
        "image",
        "supplier",
    )

admin.site.register(Bike, BikeAdmin)
