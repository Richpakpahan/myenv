from django.urls import path
from . import views

app_name='reference'

urlpatterns = [
    path('refposts/', views.ReferenceListView.as_view(), name='api_refpost_list'),
    path('refposts/<int:pk>/', views.ReferenceDetailView.as_view(), name='api_refpost_detail')
]