from django.urls import path, include
from .router import router
from . import views

urlpatterns = [
    path('', include(router.urls)),
    path('get-vehicle/<int:pk>/', views.get_vehicle, name="get-vehicle"),
    path('create-vehicle/', views.create_vehicle, name="create-vehicle"),
    path('update-vehicle/<int:pk>/', views.update_vehicle, name="update-vehicle"),
    path('delete-vehicle/<int:pk>/', views.delete_vehicle, name="delete-vehicle"),
]