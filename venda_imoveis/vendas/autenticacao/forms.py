from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, TextInput, Select, CheckboxInput, DateInput, NumberInput
from autenticacao.models import *

# formulario de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Senha')

#formulario de cadastro de cliente
class ClienteForm(ModelForm):
    """
    Formulário de cadastro de cliente.
    """
    
    class Meta:
        model = Cliente
        fields = ['nome','cpf', 'email','telefone']
        widgets = {
            'nome':TextInput(attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'telefone': NumberInput(attrs={'class': 'form-control'}),
        }
#formulario de simulacao de venda
class SimulacaoForm(ModelForm):
    """
    Formulário de simulação de venda.
    """
    
    class Meta:
        model = Venda
        fields = ['imovel','valor','corretor','cliente','condicao_pagamento']

    def __init__(self,*args,**kwargs):
        super(SimulacaoForm, self).__init__(*args, **kwargs)
        cliente = Cliente.objects.filter(ativo=True)
        imovel = Imovel.objects.filter(disponivel = True)
        self.fields['cliente'].queryset = cliente
        self.fields['imovel'].queryset = imovel
