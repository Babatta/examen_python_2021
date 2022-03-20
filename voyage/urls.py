from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('',views.home,name='acceuil'),
    path('acceuil',views.home,name='retour'),
    path('unvoyage/<str:pk>',views.index_voyage,name='unvoyage'),
    path('voyage/<str:pk>',views.index_voyage,name='voyage'),
    path('majvoyage/<str:pk>',views.modifier_voyage,name='majvoyage'),
    path('supvoyage/<str:pk>',views.supprimer_voyage,name='supvoyage'),
    path('add_voyage/<str:pk>',views.add_voyage,name='add_voyage'),
    # path('ajvoyage/<str:pk>',views.ajouter_voyage,name='ajvoyage'),
]