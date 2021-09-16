from .views import *
from django.urls import path


urlpatterns = [
    path('health/', ortho_report),
    path('ortho/', ortho_final_report)
]