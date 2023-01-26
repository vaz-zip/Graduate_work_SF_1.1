from django.urls import path
from .views import IndexView

urlpatterns = [
    path('user_list', IndexView.as_view()),
]