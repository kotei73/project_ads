from django.urls import path
from . import views


#  использование параметризованных запросов
urlpatterns = [
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('', views.index, name='index'),
    path('add/', views.AdsCreateView.as_view(), name='add'),
]