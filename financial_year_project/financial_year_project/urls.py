# financial_year_project/urls.py
from django.contrib import admin
from django.urls import path, include # Add include here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('financial-years/', include('financial_years.urls')), # Add this line
]