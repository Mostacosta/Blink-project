from django.contrib import admin
from .models import services,strategy,philosophy

# Register your models here.
admin.site.register(philosophy)
admin.site.register(strategy)
admin.site.register(services)
