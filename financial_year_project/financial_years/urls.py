# financial_years/urls.py
from django.urls import path
from . import views
from .views import FinancialYearCreateView, FinancialYearDetailView, FinancialYearUpdateView, FinancialYearDeleteView # Add FinancialYearDeleteView

urlpatterns = [
    path('', views.financial_year_list, name='financial_year_list'),
    path('add/', FinancialYearCreateView.as_view(), name='financial_year_add'),
    path('<int:pk>/', FinancialYearDetailView.as_view(), name='financial_year_detail'),
    path('<int:pk>/edit/', FinancialYearUpdateView.as_view(), name='financial_year_edit'),
    path('<int:pk>/delete/', FinancialYearDeleteView.as_view(), name='financial_year_delete'), # New: Delete URL
]