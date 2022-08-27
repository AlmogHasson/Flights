from django.urls import path
from . import views
from .views import LogoutView, MyTokenObtainPairView
 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
 
 
urlpatterns = [
    path('', views.getRoutes),
    path('customer/', views.getDetails), # profile page
    path('usertickets/', views.userTicketsPreview),
    path('addticket/', views.addTicket),
    path('register/', views.register),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('flights/', views.allFlights)
    
]
