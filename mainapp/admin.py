from django.contrib import admin
from django.conf import settings
from mainapp.models import (
    School,Teacher,Galeria, Rewiew, New
)


class SchoolAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= settings.MAX_COMPANY_COUNT:
            return False
        return super().has_add_permission(request)

admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher)
admin.site.register(Galeria)
admin.site.register(Rewiew)
admin.site.register(New)

