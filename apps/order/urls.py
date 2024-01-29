from django.urls import path, include
from .views import OrderAPIView

urlpatterns = [
    path('', OrderAPIView.as_view())
]