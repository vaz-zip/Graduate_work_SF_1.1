from django import forms
from .models import Car, TechniqueModel, EngineModel, TransmissionModel, DriveAxleModel, SteerableAxleModel, ServiceCompany, TypeOfMaintenance, TechnicalMintenance, BrokenUnit, RecoveryMethod, Complaints






class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        widgets = {
            'date_of_shipment_from_the': forms.DateInput(attrs={'type': 'date'}),
        }
        
        fields = [
            'name', 'factory_number', 'technique_model', 'engine_model', 'engine_number', 'transmission_model', 'transmission_number',
        'drive_axle_model', 'drive_axle_number', 'steerable_axle_model', 'steerable_axle_number', 'supply_contract', 'date_of_shipment_from_the',
        'consignee', 'delivery_address', 'equipment', 'client', 'service_company'
        ]



class TechniqueModelForm(forms.ModelForm):
    class Meta:
        model = TechniqueModel
        fields = [
            'name', 'description'
        ]



class EngineModelForm(forms.ModelForm):
    class Meta:
        model = EngineModel
        fields = [
            'name', 'description'
        ]



class TransmissionModelForm(forms.ModelForm):
    class Meta:
        model = TransmissionModel
        fields = [
            'name', 'description'
        ]



class DriveAxleModelForm(forms.ModelForm):
    class Meta:
        model = DriveAxleModel
        fields = [
            'name', 'description'
        ]       



class SteerableAxleModelForm(forms.ModelForm):
    class Meta:
        model = SteerableAxleModel
        fields = [
            'name', 'description'
        ]               


class TechnicalMintenanceForm(forms.ModelForm):
    class Meta:
        model = TechnicalMintenance
        widgets = {
            'date_of_maintenance': forms.DateInput(attrs={'type': 'date'}),
            'date_of_the_order' : forms.DateInput(attrs={'type': 'date'}),
        }
        
        fields = [
            'name', 'car', 'type_of_maintenance', 'date_of_maintenance', 'оperating_time', 'order', 'date_of_the_order',
            'service_company'
        ]

    
class ServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = ServiceCompany
        fields = [
            'name', 'description'
        ]



class TypeOfMaintenanceForm(forms.ModelForm):
    class Meta:
        model = TypeOfMaintenance
        fields = [
            'name', 'description'
        ]



class  BrokenUnitForm(forms.ModelForm):
    class Meta:
        model = BrokenUnit
        fields = [
            'name', 'description'
        ]



class RecoveryMethodForm(forms.ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = [
            'name', 'description'
        ]       



class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        widgets = {
            'date_of_breakdown': forms.DateInput(attrs={'type': 'date'}),
            'date_restoration' : forms.DateInput(attrs={'type': 'date'}),
            'downtime': forms.IntegerField(),
        }
        fields = [
            'name', 'date_of_breakdown', 'оperating_time', 'broken_unit', 'breakdown_description', 'recovery_method', 'spare_parts',
            'date_restoration', 'service_company', 'car'
        ]

    # def downtime(self):
    #     return (self.date_restoration - self.date_of_breakdown)
    #         'name', 'description'
                         