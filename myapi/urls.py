from django.urls import path
from .views import StatView

urlpatterns = [
    path('api/data/', StatView.as_view(), name='data-api'),
]