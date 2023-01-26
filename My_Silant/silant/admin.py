from django.contrib import admin
from .models import Car, TechniqueModel, Complaints, ServiceCompany, EngineModel, TransmissionModel, DriveAxleModel, SteerableAxleModel, ServiceCompany, TypeOfMaintenance, TechnicalMintenance, BrokenUnit, RecoveryMethod, CarComplaints



admin.site.register(Car)
admin.site.register(Complaints)
admin.site.register(TechniqueModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteerableAxleModel)
admin.site.register(ServiceCompany)
admin.site.register(TypeOfMaintenance)
admin.site.register(TechnicalMintenance)
admin.site.register(BrokenUnit)
admin.site.register(RecoveryMethod)
# admin.site.register(CarTechnicalMintenance)
# admin.site.register(CarComplaints)