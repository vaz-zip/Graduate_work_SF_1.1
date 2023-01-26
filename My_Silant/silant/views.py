from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views.generic import CreateView, DetailView
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .models import Car, Complaints
from .forms import CarForm, TechniqueModelForm, EngineModelForm, TransmissionModelForm, DriveAxleModelForm, SteerableAxleModelForm, ServiceCompanyForm, TypeOfMaintenanceForm, TechnicalMintenanceForm, BrokenUnitForm, RecoveryMethodForm, ComplaintsForm
from .filters import CarFilter, TechnicalMintenanceFilter, ComplaintsFilter
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, CreateView):
    template_name = 'index.html'
    form_class = CarForm

    def get_success_url(self) -> str:
        return '/admin/'


# добавить в справочник модель техники
class TechniqueModelView(LoginRequiredMixin, CreateView):
    template_name = 'technique_model.html'
    form_class = TechniqueModelForm


class EngineModelView(LoginRequiredMixin, CreateView):
    template_name = 'engine_model.html'
    form_class = EngineModelForm

    def get_success_url(self) -> str:
        return '/default1'


class TransmissionModelView(LoginRequiredMixin, CreateView):
    template_name = 'transmission_model.html'
    form_class = TransmissionModelForm

    def get_success_url(self) -> str:
        return '/admin/'


class DriveAaxleModelView(LoginRequiredMixin, CreateView):
    template_name = 'drive_axle_model.html'
    form_class = DriveAxleModelForm

    def get_success_url(self) -> str:
        return '/admin/'


class SteerableAxleModelView(LoginRequiredMixin, CreateView):
    template_name = 'steerable_axle_model.html'
    form_class = SteerableAxleModelForm

    def get_success_url(self) -> str:
        return '/admin/'


class ServiceCompanyView(LoginRequiredMixin, CreateView):
    template_name = 'service_company.html'
    form_class = ServiceCompanyForm

    def get_success_url(self) -> str:
        return '/admin/'


class TypeOfMaintenanceView(LoginRequiredMixin, CreateView):
    template_name = 'type_of_maintenance.html'
    form_class = TypeOfMaintenanceForm

    def get_success_url(self) -> str:
        return '/admin/'


class TechnicalMintenanceView(LoginRequiredMixin, CreateView):
    template_name = 'technical_mintenance.html'
    form_class = TechnicalMintenanceForm

    def get_success_url(self) -> str:
        return '/admin/'


class BrokenUnitView(LoginRequiredMixin, CreateView):
    template_name = 'broken_unit.html'
    form_class = BrokenUnitForm

    def get_success_url(self) -> str:
        return '/admin/'


class RecoveryMethodView(LoginRequiredMixin, CreateView):
    template_name = 'recovery_method.html'
    form_class = RecoveryMethodForm

    def get_success_url(self) -> str:
        return '/admin/'


class ComplaintsView(LoginRequiredMixin, CreateView):
    template_name = 'complaints.html'
    form_class = ComplaintsForm

    def get_success_url(self) -> str:
        return '/admin/'


# class CarList(ListView):
#     model = Car
#     ordering = 'name'
#     template_name = 'cars.html'
#     context_object_name = 'cars'
#     queryset = Car.objects.all()
#     # paginate_by = 3


class CarList(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())  # фильтр поиска
        return context


class DefaultList(ListView):
    model = Car
    template_name = 'default.html'
    context_object_name = 'cars1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class DefaultListOne(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'default2.html'
    context_object_name = 'cars2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class SearchResultsView(ListView):
    model = Car
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Car.objects.filter(
            Q(factory_number=query) | Q(
                technique_model=query) | Q(engine_model=query)
            | Q(engine_number=query) | Q(transmission_model=query) | Q(transmission_number=query)
            | Q(drive_axle_model=query) | Q(drive_axle_number=query) | Q(steerable_axle_model=query)
            | Q(steerable_axle_number=query)
        )
        return object_list

# class SearchClientView(LoginRequiredMixin, DetailView):
#     model = Car
#     template_name = 'search_client.html'
#     context_object_name = 'object_list'
    
#     def get_object(self, **kwargs):
#         id = self.kwargs.get('pk')
#         return Car.objects.get(pk=id)

class SearchClientView(ListView):
    model = Car
    template_name = 'search_cient.html'

    def get_queryset(self):
        query = self.request.GET.get('qc')
        object_list = Car.objects.filter(
            Q(factory_number=query) | Q(
                technique_model=query) | Q(engine_model=query)
            | Q(engine_number=query) | Q(transmission_model=query) | Q(transmission_number=query)
            | Q(drive_axle_model=query) | Q(drive_axle_number=query) | Q(steerable_axle_model=query)
            | Q(steerable_axle_number=query)
        )
        return object_list        


class CarDetail(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'my_car.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Car.objects.get(pk=id)


class TechnicalMintenanceList(LoginRequiredMixin, ListView):
    model = TechnicalMintenance
    template_name = 'tm_list.html'
    context_object_name = 'tm'
    # paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TechnicalMintenanceFilter(
            self.request.GET, queryset=self.get_queryset())  # фильтр поиска
        return context


class TechnicalMintenanceDetail(LoginRequiredMixin, DetailView):
    model = TechnicalMintenance
    template_name = 'tm_car.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return TechnicalMintenance.objects.get(pk=id)


class ComplaintsList(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = 'complaints_list.html'
    context_object_name = 'comp_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ComplaintsFilter(
            self.request.GET, queryset=self.get_queryset())  # фильтр поиска
        return context


class ComplaintsDetail(LoginRequiredMixin, DetailView):
    model = Complaints
    template_name = 'complaints_detail.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Complaints.objects.get(pk=id)
