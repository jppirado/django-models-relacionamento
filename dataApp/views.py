
from peopleApp.models import People , Contato
from  django.views.generic import UpdateView , ListView, CreateView, DeleteView
from  .forms import PeopleForm , ContatoForm 
from django.shortcuts import render , redirect , reverse , get_object_or_404 




# Create your views here.
class ListaPessoaView( ListView ) : 
  model = People
  queryset =  People.objects.all().order_by('nome_completo')
  
  def get_queryset(self) : 
      queryset = super().get_queryset()
      filtro_nome = self.request.GET.get('nome')or None
      filtro_data = self.request.GET.get('data') or None

      if filtro_nome:
          queryset = queryset.filter(nome_completo__contains =  filtro_nome)
          return queryset

      if filtro_data :
          queryset = queryset.filter ( data_nascimento =  filtro_data )  
          return queryset  

      return queryset     

class PesoaCreateView( CreateView ) :
  model = People
  form_class = PeopleForm
  success_url = '/pessoas/'

class PessoaUpdateView( UpdateView ) :
  model = People
  form_class = PeopleForm
  success_url = '/pessoas/'

class PessoaDeleteView( DeleteView ) : 
  model = People 
  success_url = '/pessoas/'

def contatos(request , pk_pessoa):
  contatos = Contato.objects.filter(pessoa=pk_pessoa)
  return render( request , "contato/contato_list.html" , {'contatos' : contatos , 'pk' :  pk_pessoa})    

def contato_novo( request , pk_pessoa): 
  form = ContatoForm()
  if request.method == "POST":
    form = ContatoForm(request.POST)
    if form.is_valid():
      contato = form.save(commit=False)
      contato.pessoa_id = pk_pessoa
      contato.save() 
      return redirect(reverse('pessoa.contatos' , args={pk_pessoa}))
  return render(request , 'contato/contato_form.html' , {'form' : form})    

def contato_editar( request , pk_pessoa, pk):
  contato = get_object_or_404(Contato, pk=pk)
  form = ContatoForm(instance=contato)
  if request.method == "POST":
    form = ContatoForm( request.POST , instance=contato )
    if form.is_valid():
      form.save() 
      return redirect(reverse('pessoa.contatos' , args=[pk_pessoa]))
  return render( request , 'contato/contato_form.html' , {'form' :  form } )

def contato_remover( request , pk_pessoa , pk ):
  contato = get_object_or_404(Contato, pk=pk)
  contato.delete() 
  return redirect( reverse( 'pessoa.contatos ', args=[pk_pessoa])) 


