from __future__ import annotations

from django.db import models
from django.utils import timezone

class ClienteQuerySet(models.QuerySet):
    def ativos(self):
        return self.filter(archived_at__isnull=True)
    
    def arquivados(self):
        return self.filter(archived_at__isnull=False)
    
class Cliente(models.Model):
    class TipoDocumento(models.TextChoices):
        CPF = "CPF", "CPF"
        CNPJ = "CNPJ", "CNPJ"

    nome = models.CharField(max_length=120)
    tipo_documento = models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CPF)
    documento = models.CharField(max_length=18, help_text="Armazene sem máscara (apenas números).")
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    cep = models.CharField(max_length=8, blank=True)
    endereco = models.CharField(max_length=160, blank=True)
    numero = models.CharField(max_length=20, blank=True)
    complemento = models.CharField(max_length=160, blank=True)
    bairro = models.CharField(max_length=160, blank=True)
    cidade = models.CharField(max_length=160, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(null=True, blank=True)

    objects = ClienteQuerySet.as_manager

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["nome"]),
            models.Index(fields=["documento"]),
            models.Index(fields=["email"]),
        ]
        constraints = [
            models.UniqueConstraint(fields=["documento"], name="uniq_cliente_documento"),
        ]

    def _str_(self) -> str: 
        return f"{self.nome} ({self.documento})"
    
    @property
    def is_arquivado(self) -> bool:
        return self.archived_at is not None
    
    def arquivar(self):
        if not self.archived_at:
            self.archived_at = timezone.now()
            self.save(update_fields=["archived_at"])

    def reativar(self):
        if self.archived_at:
            self.archived_at = None
            self.save(update_fields=["achived_at"])