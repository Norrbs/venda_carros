from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Carro
from .forms import CarroForm
from django.contrib import messages
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView, CreateView

# Create your views here.

class HomeTemplateView(TemplateView):
  template_name = "home.html"

# def home(request):
#   return render(request, 'home.html')

class ListarTemplateView(ListView):
  model = Carro
  template_name = 'listar.html'
  context_object_name = 'carros'
  ordering = 'modelo'


# def listar(request):
#   carros = Carro.objects.all().order_by('modelo')
#   return render(request, 'listar.html',{'carros':carros})

class DetalharTemplateView(DetailView):
  model = Carro
  template_name = 'detalhar.html'
  context_object_name = 'carro'

# def detalhar(request,id):
#   carro = Carro.objects.get(id=id)
#   return render(request, 'detalhar.html',{'carro':carro})

class AdicionarTemplateView(CreateView):
  model = Carro
  template_name = 'adicionar.html'
  context_object_name = 'carro'
  form_class = CarroForm

  def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro atualizado com sucesso!")
        return reverse('listar')

# def adicionar(request):
#   if request.method == 'POST':
#     form = CarroForm(request.POST, request.FILES)
#     if form.is_valid():
#       form.save()
#       messages.add_message(request, messages.SUCCESS, "Carro adicionado com sucesso!")
#       return redirect('listar')
#   else:
#     form = CarroForm()
#     return render(request, 'adicionar.html',{'form':form})

class AtualizarTemplateView(UpdateView):
  model = Carro
  template_name = 'atualizar.html'
  context_object_name = 'carro'
  form_class = CarroForm

  def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro atualizado com sucesso!")
        return reverse('listar')

# def atualizar(request,id):
#   carro = Carro.objects.get(id=id)
#   form = CarroForm(instance=carro)
#   if request.method == 'POST':
#     form = CarroForm(request.POST, request.FILES, instance=carro)
#     if form.is_valid():
#       form.save()
#       messages.add_message(request, messages.INFO, "Informações do carro foram atualizadas")
#       return redirect('listar')
#     else:
#       return render(request, 'atualizar.html', {'form':form})
#   else:
#     return render(request, 'atualizar.html', {'form':form})

class DeletarTemplateView(DeleteView):
    model=Carro

  #  def get_success_url(self):
  #       messages.add_message(self.request, messages.SUCCESS, "Carro deletado com sucesso!")
  #       return reverse('listar')

# def deletar(request,id):
#   carro = Carro.objects.get(id=id)
#   carro.delete()
#   messages.add_message(request, messages.INFO, "Carro removido")
#   return redirect('listar')

