from django.urls import path
from .views import save_student

urlpatterns = [
    path('save_student/', save_student, name='save_student'),
]
