from django.contrib import admin
from .models import Projects,Institue
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/text-editor.js",)

admin.site.register(Projects,ProjectAdmin)
admin.site.register(Institue)

