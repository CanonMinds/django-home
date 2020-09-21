from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)

from . import mixins
from . import models

# Create your views here.

# def team_list(request):
#     teams = models.Team.objects.all()
#     return render(request, 'teams/team_list.html', {'teams': teams})


# def team_detail(request, pk):
#     team = get_object_or_404(models.Team, pk=pk)
#     return render(request, 'teams/team_detail.html', {'team': team})


class TeamListView(CreateView, ListView):
    context_object_name = "teams"
    fields = ("name", "field_location", "lead")
    model = models.Team
    template_name = "teams/team_list.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["lead"] = self.request.user.pk
        return initial

class TeamDetailView(DetailView, UpdateView):
    fields = ("name", "field_location", "lead")
    model = models.Team
    template_name = "teams/team_detail.html"

class TeamCreateView(LoginRequiredMixin, mixins.PageTitleMixin, mixins.SuccessMessageMixin, CreateView):
    fields = ("name", "field_location", "lead")
    model = models.Team
    page_title = "Create a new service"

    def get_initial(self):
        initial = super().get_initial()
        initial["lead"] = self.request.user.pk
        return initial

class TeamUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, mixins.SuccessMessageMixin, UpdateView):
    fields = ("name", "field_location", "lead")
    model = models.Team

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.name)

    def get_success_message(self):
        obj = self.get_object()
        return "{} was successfully updated!".format(obj.name)

class TeamDeleteView(LoginRequiredMixin,  DeleteView):
    model = models.Team
    # succes_url = reverse_lazy("teams:list")

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(lead=self.request.user)
        return self.model.objects.all()

    def get_success_url(self):
        # return reverse('teams:list', kwargs={'pk': self.object.pk})