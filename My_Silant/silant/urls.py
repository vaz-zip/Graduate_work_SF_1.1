from django.urls import path
from .views import *


urlpatterns = [
    path('', DefaultList.as_view()),
    path('default1', DefaultListOne.as_view(), name='user_list'),
    path('car_list', CarList.as_view(), name='car_list'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('search_client', SearchClientView.as_view(), name='search_clients'),
    # path('car_list', CarList.as_view()),
    path('<int:pk>', CarDetail.as_view(), name='my_car'),
    path('tm_list', TechnicalMintenanceList.as_view()),
    path('tm_car<int:pk>', TechnicalMintenanceDetail.as_view(), name='tm_detail'),
    path('index', Index.as_view(), name='index'),
    path('complaints_list', ComplaintsList.as_view()),
    path('complaints_detail<int:pk>', ComplaintsDetail.as_view(), name='comp_detail'),

    path('index', Index.as_view()),
    path('technique_model', TechniqueModelView.as_view()),
    path('engine_model', EngineModelView.as_view()),
    path('transmission_model', TransmissionModelView.as_view()),
    path('drive_axle_model', DriveAaxleModelView.as_view()),
    path('steerable_axle_model', SteerableAxleModelView.as_view()),
    path('service_company', ServiceCompanyView.as_view()),
    path('type_of_maintenance', TypeOfMaintenanceView.as_view()),
    path('technical_mintenance', TechnicalMintenanceView.as_view()),
    path('broken_unit', BrokenUnitView.as_view()),
    path('recovery_method', RecoveryMethodView.as_view()),
    path('complaints', ComplaintsView.as_view()),
    
    # path('technique_model', TechniqueModelView.as_view()),
    # path('engine_model', EngineModelView.as_view()),
    # path('transmission_model', TransmissionModelView.as_view()),
    # path('drive_axle_model', DriveAaxleModelView.as_view()),
    # path('steerable_axle_model', SteerableAxleModelView.as_view()),
    # path('service_company', ServiceCompanyView.as_view()),
    # path('type_of_maintenance', TypeOfMaintenanceView.as_view()),
    # path('technical_mintenance', TechnicalMintenanceView.as_view()),
    # path('broken_unit', BrokenUnitView.as_view()),
    # path('steerable_axle_model', RecoveryMethodView.as_view())
    
]