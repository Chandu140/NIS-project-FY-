from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint, Q # Import UniqueConstraint and Q

class FinancialYear(models.Model):
    # Choices for Budget Source
    BUDGET_SOURCE_COMMITTED = 'COMMITTED'
    BUDGET_SOURCE_DPIP = 'DPIP'
    BUDGET_SOURCE_CHOICES = [
        (BUDGET_SOURCE_COMMITTED, 'Committed'),
        (BUDGET_SOURCE_DPIP, 'Dpip'),
    ]

    name = models.CharField(max_length=9, unique=False) # Remove unique=True here, as uniqueness is now combined
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # New field for Budget Source
    budget_source = models.CharField(
        max_length=10,
        choices=BUDGET_SOURCE_CHOICES,
        default=BUDGET_SOURCE_DPIP, # Set a default if desired
        help_text="Select the budget source."
    )

    class Meta:
        verbose_name = "Financial Year"
        verbose_name_plural = "Financial Years"
        # ordering = ['-start_date'] # Order by start date descending
        
        # Add the UniqueConstraint here
        constraints = [
            UniqueConstraint(fields=['name', 'budget_source'], name='unique_financial_year_budget_source')
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('financial_year_detail', kwargs={'pk': self.pk})