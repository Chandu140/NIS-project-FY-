# financial_years/views.py
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView # Add DeleteView
from django.urls import reverse_lazy
from .models import FinancialYear
from .forms import FinancialYearForm

def financial_year_list(request):
    financial_years = FinancialYear.objects.all().order_by('-start_date')
    context = {
        'financial_years': financial_years,
        'page_title': 'Financial Year Management'
    }
    return render(request, 'financial_years/financial_year_list.html', context)

class FinancialYearCreateView(CreateView):
    model = FinancialYear
    form_class = FinancialYearForm
    template_name = 'financial_years/financial_year_form.html'
    success_url = reverse_lazy('financial_year_list')

class FinancialYearDetailView(DetailView):
    model = FinancialYear
    template_name = 'financial_years/financial_year_detail.html'
    context_object_name = 'year'

class FinancialYearUpdateView(UpdateView):
    model = FinancialYear
    form_class = FinancialYearForm
    template_name = 'financial_years/financial_year_form.html'
    success_url = reverse_lazy('financial_year_list')

# New: Class-based view for deleting a financial year
class FinancialYearDeleteView(DeleteView):
    model = FinancialYear
    template_name = 'financial_years/financial_year_confirm_delete.html' # We will create this template next
    success_url = reverse_lazy('financial_year_list') # Redirect to list page after successful deletion
    context_object_name = 'year' # The variable name to use in the template