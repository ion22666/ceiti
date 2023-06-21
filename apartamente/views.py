from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Agent
from .forms import AgentForm

# Create your views here.
# Functional based view
# Create a apartament
# def apartament_create(request):
#     if request.method == "POST":
#         form = AgentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("apartament_list"))
#     else:
#         form = AgentForm()
#
#     return render(request, "apartament/apartament_form.html", { "form": form, })
#
#
# # Retrieve apartament list
# def apartament_list(request):
#     apartament = Agent.objects.all()
#     return render(request, "apartament/apartament_list.html", { "apartament": apartament,})
#
#
# # Retrieve a single apartament
# def apartament_detail(request, pk):
#     apartament = get_object_or_404(Agent, pk=pk)
#     return render(request, "apartament/apartament_detail.html", { "apartament": apartament, })
#
#
# # Update a single apartament
# def apartament_update(request, pk):
#     apartament_obj = get_object_or_404(Agent, pk=pk)
#     if request.method == 'POST':
#         form = AgentForm(instance=apartament_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("apartament_detail", args=[pk,]))
#     else:
#         form = AgentForm(instance=apartament_obj)
#
#     return render(request, "apartament/apartament_form.html", { "form": form, "object": apartament_obj})
#
#
# # Delete a single apartament
# def apartament_delete(request, pk):
#     apartament_obj = get_object_or_404(Agent, pk=pk)
#     apartament_obj.delete()
#     return redirect(reverse("apartament_list"))

# Class Based Views
from django.views import generic
from .models import Apartament, Agent
from .forms import ApartamentForm, AgentForm
# APARTAMENTE
class ApartamentListView(generic.ListView):
    model = Apartament
    template_name  = 'apartament_list.html'
    context_object_name = 'apartamente'

class ApartamentDetailView(generic.DetailView):
    model = Apartament
    template_name  = 'apartament_detail.html'

class ApartamentCreateView(generic.CreateView):
    model = Apartament
    form_class = ApartamentForm
    template_name  = 'apartament_form.html'
    success_url = '/apartamente'

class ApartamentUpdateView(generic.UpdateView):
    model = Apartament
    form_class = ApartamentForm
    template_name  = 'apartament_form.html'
    success_url = '/apartamente'

class ApartamentDeleteView(generic.DeleteView):
    model = Apartament
    template_name  = 'apartament_confirm_delete.html'
    success_url = '/apartamente'



# AGENTI
class AgentListView(generic.ListView):
    model = Agent
    context_object_name = 'agents'

class AgentDetailView(generic.DetailView):
    model = Agent

class AgentCreateView(generic.CreateView):
    model = Agent
    form_class = AgentForm
    success_url = reverse_lazy('agent_list.html')

class AgentUpdateView(generic.UpdateView):
    model = Agent
    form_class = AgentForm
    success_url = reverse_lazy('agent_list.html')

class AgentDeleteView(generic.DeleteView):
    model = Agent
    success_url = reverse_lazy('agent_list.html')