from django.urls import path
from .views import StatView

urlpatterns = [
    path('data/general-general', GeneralGeneralView.as_view(), name='general-general-data'),
    path('data/general-domicil', GeneralDomicilView.as_view(), name='general-domicil-data'),
    path('data/general-exterieur', GeneralExterieurView.as_view(), name='general-exterieur-data'),
    path('data/defense-general', DefenseGeneralView.as_view(), name='defense-general'),
    path('data/defense-domicil', DefenseDomicilView.as_view(), name='defense-domicil'),
    path('data/defense-exterieur', DefenseExterieurView.as_view(), name='defense-exterieur'),
    path('data/attaque-general', AttaqueGeneralView.as_view(), name='attaque-general'),
    path('data/attaque-domicil', AttaqueDomicilView.as_view(), name='attaque-domicil'),
    path('data/attaque-exterieur', AttaqueExterieurView.as_view(), name='attaque-exterieur'),
]