from django.contrib import admin
from .models import home_cover,project_image,project
# Register your models here.

admin.site.register(home_cover)
admin.site.register(project_image)


class project_image_Inline(admin.TabularInline):
    model = project_image

class projectAdmin(admin.ModelAdmin):
    inlines = [
        project_image_Inline,
    ]

admin.site.register(project,projectAdmin)