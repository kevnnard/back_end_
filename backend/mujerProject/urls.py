from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from mujerApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/',views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),

    path('centro/create/', views.CentroCreateView.as_view()),
    path('centro/delete/<int:pk>/', views.CentroDeleteView.as_view()),
    path('centro/put/<int:pk>/', views.CentroPutView.as_view()),
    path('centro/get/<int:pk>/', views.CentroGetView.as_view()),
    path('centro/get/', views.CentroGetAllView.as_view()),

    path('solicitud/create/', views.SolicitudCreateView.as_view()),
    path('solicitud/delete/<int:pk>/', views.SolicitudDeleteView.as_view()),
    path('solicitud/put/<int:pk>/', views.SolicitudPutView.as_view()),
    path('solicitud/get/<int:pk>/', views.SolicitudGetView.as_view()),
    path('solicitud/get/', views.SolicitudGetAllView.as_view()),
]
