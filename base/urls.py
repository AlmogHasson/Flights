from django.urls import path
from . import views
from .views import MyTokenObtainPairView
 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
 
 
urlpatterns = [
    path('', views.getRoutes),
    path('customer/', views.getDetails),
    path('usertickets/', views.userTicketsPreview),
    path('addticket/', views.addTicket),
    path('register/', views.register),
 
 
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
