"""vendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

from autenticacao.views import ResumoView,SimulacaoView,ListaUnidadesView,ListagemClientesView, CadastrarClienteView, DeletarClienteView,EditarClienteView
from autenticacao.forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('listagem-clientes/', ListagemClientesView.as_view(), name='listagem-clientes'), 
    path('cadastro-clientes/', CadastrarClienteView.as_view(), name='cadastrar-clientes'),
    path('deletar-cliente/', DeletarClienteView.as_view(), name='deletar-cliente'),
    path('editar-cliente/<slug:pk>', EditarClienteView.as_view(), name='editar-cliente'),
    path('recibo/<slug:pk>', ResumoView.as_view(), name='recibo'),
    path('listagem-unidades/', ListaUnidadesView.as_view(), name='listagem-unidades'), 
    path('simulacao/', SimulacaoView.as_view(), name='simulacao'), 

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

