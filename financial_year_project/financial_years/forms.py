# financial_years/forms.py
import re
from datetime import date
from django import forms
from .models import FinancialYear

class FinancialYearForm(forms.ModelForm):
    # Define choices for the financial year name field
    FINANCIAL_YEAR_CHOICES = [
        ('', 'Select Financial Year'), # Added default blank option
        ('2024-2025', '2024-2025'),
        ('2025-2026', '2025-2026'),
    ]

    # Override the 'name' field from the model to be a ChoiceField
    name = forms.ChoiceField(
        choices=FINANCIAL_YEAR_CHOICES,
        label="Financial Year",
        # help_text="Select the financial year.",
        required=True # Ensure it's still required, so user must pick a valid year
    )

    # Override the 'budget_source' field from the model to be a ChoiceField
    # so we can add the default blank option.
    budget_source = forms.ChoiceField(
        choices=[('', 'Select Budget Source')] + list(FinancialYear.BUDGET_SOURCE_CHOICES), # Added default blank option
        label="Budget Source",
        # help_text="Select the budget source.",
        required=True # Ensure it's still required
    )


    class Meta:
        model = FinancialYear
        fields = ['name', 'start_date', 'end_date', 'is_active', 'budget_source']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Custom __init__ to handle instance data for ChoiceField
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # For 'name' field
            if self.instance.name in [choice[0] for choice in self.FINANCIAL_YEAR_CHOICES]:
                self.initial['name'] = self.instance.name
            else:
                # If existing name is not in predefined choices, set to blank.
                # User will need to re-select a valid option if editing.
                self.initial['name'] = '' 
            
            # For 'budget_source' field
            # Check if the instance's budget_source is one of the valid choices (excluding the blank one)
            valid_budget_sources = [choice[0] for choice in FinancialYear.BUDGET_SOURCE_CHOICES]
            if self.instance.budget_source in valid_budget_sources:
                self.initial['budget_source'] = self.instance.budget_source
            else:
                self.initial['budget_source'] = ''


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        budget_source = cleaned_data.get('budget_source')

        # Check if "Select Financial Year" or "Select Budget Source" were submitted
        if not name: # This checks if the blank option was selected for 'name'
            self.add_error('name', "Please select a financial year.")
        
        if not budget_source: # This checks if the blank option was selected for 'budget_source'
            self.add_error('budget_source', "Please select a budget source.")

        # Only proceed with date and budget_source logic if name is valid
        if name and start_date and end_date:
            try:
                # Extract years from financial year name (e.g., "2024-2025")
                match = re.match(r'(\d{4})-(\d{4})$', name)
                if not match:
                    # Should not happen if name is a ChoiceField, but good for robustness
                    self.add_error('name', "Financial year name format is incorrect. Use 'YYYY-YYYY'.")
                    return cleaned_data # Exit clean if name format is bad

                start_year_name = int(match[1])
                end_year_name = int(match[2])

                # Validate year sequence in name
                if end_year_name != start_year_name + 1:
                    self.add_error('name', "Financial year name must span consecutive years (e.g., 2024-2025).")


                # Validate start_date and end_date based on name
                expected_start_date = date(start_year_name, 4, 1)  # April 1st
                expected_end_date = date(end_year_name, 3, 31)    # March 31st

                if start_date != expected_start_date:
                    self.add_error('start_date', f"Start date must be April 1st of {start_year_name}.")
                if end_date != expected_end_date:
                    self.add_error('end_date', f"End date must be March 31st of {end_year_name}.")

            except (ValueError, TypeError):
                self.add_error('name', "Invalid financial year name selected.")

        # Server-side validation for BudgetSource based on the financial year name
        # Only perform this if both name and budget_source are valid (not blank)
        if name == '2024-2025' and budget_source == FinancialYear.BUDGET_SOURCE_COMMITTED:
            self.add_error('budget_source', "For Financial Year 2024-2025, 'Committed' budget source is not allowed.")

        return cleaned_data