from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Car, TechnicalMintenance, Complaints
 
 
class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = (
            'technique_model', 'engine_model', 'transmission_model', 'drive_axle_model', 'steerable_axle_model',
            )
 

class CarSearchFiltr(FilterSet):
    class Meta:
        model = Car
        fields = (
            'factory_number',
        )


class TechnicalMintenanceFilter(FilterSet):
    class Meta:
        model = TechnicalMintenance
        fields = (
            'type_of_maintenance', 'service_company', 'car',
            )


# class CarNumberFilter(FilterSet):
#     class Meta:
#         maodel = Car
#         fields = (
#             'engine_model',
#         )            


class ComplaintsFilter(FilterSet):
    class Meta:
        model = Complaints
        fields = (
            'broken_unit', 'recovery_method', 'service_company',
            )