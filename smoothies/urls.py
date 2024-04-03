from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_smoothies, name='smoothies'),
    path('<name>', views.smoothie_detail, name='smoothie_detail'),
]