from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import (
    Person
)

@admin.register(
    Person,
)

class UniversalAdmin(ImportExportMixin, admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
