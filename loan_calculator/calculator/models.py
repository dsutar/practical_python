from django.db import models

class LoanScenario(models.Model):
    """
    LoanScenario model represents a loan scenario with various financial details.
    """
  
    purchase_price = models.FloatField()
    down_payment = models.FloatField()
    down_payment_type = models.CharField(max_length=10, choices=[('percent', 'Percent'), ('dollar', 'Dollar')])
    mortgage_term = models.IntegerField()
    term_unit = models.CharField(max_length=10, choices=[('years', 'Years'), ('months', 'Months')]) 
    interest_rate = models.FloatField()
    monthly_payment = models.FloatField(null=True, blank=True)
    annual_payment = models.FloatField(null=True, blank=True)
    total_payment = models.FloatField(null=True, blank=True) # total payment paid over the life of the loan
    total_interest = models.FloatField(null=True, blank=True) # total interest paid over the life of the loan
    created_at = models.DateTimeField(auto_now_add=True)
