from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "nome",
            "tipo_documento",
            "documento",
            "email",
            "telefone",
            "cep",
            "endereco",
            "numero",
            "complemento",
            "bairro",
            "cidade",
            "estado",
        ]

    def clean_documento(self):
        doc = (self.cleaned_data.get("documento") or "").strip()
        doc = "".join(ch for ch in doc if ch.isdigit())
        return doc
    