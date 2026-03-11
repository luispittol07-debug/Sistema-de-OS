from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["nome", "email", "telefone", "cpf_cnpj"]

        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome do cliente"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "email@email.com"}
            ),
            "telefone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "(55) 99999-9999",
                    "id": "telefone",
                }
            ),
            "cpf_cnpj": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "cpf_cnpj",
                    "placeholder": "CPF ou CNPJ",
                }
            ),
        }