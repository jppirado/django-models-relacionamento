from django.urls import path
from .views import PessoaDeleteView ,   ListaPessoaView , PessoaUpdateView, PesoaCreateView

from .views import  contatos , contato_novo , contato_editar , contato_remover

urlpatterns = [
     path('' ,ListaPessoaView.as_view() , name="pessoa.index" ),
     path('novo/' ,   PesoaCreateView.as_view(), name="pessoa.novo" ),
     path('<int:pk>/alterar' , PessoaUpdateView.as_view( ) , name="pessoa.alterar"),
     path('<int:pk>/remover' , PessoaDeleteView.as_view( ) , name="pessoa.remover"),
     path('<int:pk_pessoa>/contato' , contatos , name="pessoa.contatos"),
     path('<int:pk_pessoa>/contatos/novo' , contato_novo , name="contato.novo"), 
     path('<int:pk_pessoa>/contato/<int:pk>/editar' , contato_editar , name="contato.editar"),
     path('<int:pk_pessoa>/contato/<int:pk>/remover' , contato_remover , name="contato.remover"),
     
]
