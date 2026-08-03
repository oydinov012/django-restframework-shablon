from rest_framework.routers import DefaultRouter
from api.views.user_app import UserModeViewSet
from django.urls import path, include
from api.views.product_view import CalculateAPIView

r = DefaultRouter()

r.register(r'users', UserModeViewSet, basename='users')

urlpatterns = [
    path('', include(r.urls)),
    path('calculate/',CalculateAPIView.as_view(),name='calculate-view'),
]
