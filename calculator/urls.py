from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main),
    path('<recipes_name>/', views.get_recipes_tool),
]
