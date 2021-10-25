from django.http.response import JsonResponse
from django.views.generic import UpdateView, View, FormView, ListView, CreateView, DetailView, DeleteView
from django.shortcuts import render,redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Cliente, Venda, Imovel
from .forms import ClienteForm, SimulacaoForm
from django.contrib import messages
from django.contrib.auth.models import User



class ListagemClientesView(ListView):
    model = Cliente
    template_name = "listagem_clientes.html"

    def get(self, request):
        ctx = {}
        cliente = Cliente.objects.filter(ativo=True).order_by('nome')
        ctx['clientes'] = cliente

        return render(self.request, self.template_name, ctx)

class CadastrarClienteView(CreateView):
    model = Cliente
    template_name = "cadastro_clientes.html"

    def get(self, request):
        form = ClienteForm()
        ctx = {'form':form}
        return render(self.request, self.template_name, ctx)

    def post(self, request):
        form = ClienteForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect('listagem-clientes')
        else:
            form = ClienteForm()
            ctx = {'form':form}
            messages.error(self.request, 'CPF já existe no sistema.')
            print('foi no else')
            print(form.errors)
            return render(self.request, self.template_name, ctx)

class DeletarClienteView(View):
    def get(self, request):
        ctx = {}
        cliente = request.GET.get('cliente')
        print(cliente)

        usuario = Cliente.objects.filter(id=cliente).first()
        print(usuario)

        usuario.ativo = False
        usuario.save()        

        return JsonResponse({},safe=False)

class EditarClienteView(UpdateView):
    model = Cliente
    fields = ['nome','cpf','email','telefone']
    template_name = "editar_clientes.html"
    success_url="/listagem-clientes"

class ListaUnidadesView(ListView):
    model = Imovel  
    template_name = "listagem_unidades.html"

    def get(self, request):
        ctx = {}
        venda_form = SimulacaoForm()
        imovel = Imovel.objects.filter(ativo=True).order_by('valor')
        ctx['imoveis'] = imovel
        ctx['venda'] = venda_form

        return render(self.request, self.template_name, ctx)

class SimulacaoView(View):
    def get(self, request):
        ctx = {}
        imovel = request.GET.get('imovel')
        valor = request.GET.get('valor')
        corretor = request.GET.get('corretor')
        cliente = request.GET.get('cliente')
        forma_pagamento = request.GET.get('forma_pagamento')

        imovel_ = Imovel.objects.get(id=imovel)
        corretor_ = User.objects.get(id=corretor)
        cliente_ = Cliente.objects.get(id=cliente)

        print(imovel)
        print(valor)
        print(corretor)
        print(cliente)
        print(forma_pagamento)

        venda = Venda.objects.create(
            imovel = imovel_,
            valor = valor,
            corretor = corretor_,
            cliente = cliente_,
            condicao_pagamento = forma_pagamento
        )
        
        return JsonResponse({},safe=False)

class ResumoView(ListView):
    model = Venda  
    template_name = "recibo.html"

    def get(self, request,pk):
        ctx = {}
        imovel = Imovel.objects.filter(id=pk, ativo=True).first()
        print(imovel)
        venda = Venda.objects.filter(ativo=True, imovel=imovel)
        print(venda)

        ctx['vendas'] = venda

        return render(self.request, self.template_name, ctx)