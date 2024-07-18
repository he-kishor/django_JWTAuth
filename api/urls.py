from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

from .views import MyTokenobtainpPairView, Registrationview,dashbord
urlpatterns = [
    path('token/',MyTokenobtainpPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path("register/",Registrationview.as_view()),
    path("dashbord/", dashbord)
]
