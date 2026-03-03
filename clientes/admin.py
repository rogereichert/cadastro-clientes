from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "documento", "email", "telefone", "archived_at", "created_at")
    list_filter = ("tipo_documento", "archived_at")
    search_fields = ("nome", "documento", "email")
    ordering = ("-created_at",)