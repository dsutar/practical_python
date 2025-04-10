import requests
"""
LoanScenarioViewSet handles CRUD operations for LoanScenario model.
Methods:
    perform_create(serializer):
        Overrides the default perform_create method to calculate loan details
        and fetch additional data from an external API before saving the instance.
        Args:
            serializer (LoanScenarioSerializer): The serializer instance containing
            the validated data.
        Raises:
            ValidationError: If there is an error fetching data from the external API.
        The method performs the following steps:
        1. Calculates the loan amount based on purchase price and down payment.
        2. Converts the mortgage term to months if necessary.
        3. Makes a GET request to the API Ninjas mortgage calculator endpoint with
           the loan amount, interest rate, and term in months.
        4. If the API response is successful, extracts the monthly payment, annual
           payment, and total interest paid from the response.
        5. Calculates the total payment by multiplying the monthly payment by the
           term in months.
        6. Saves the LoanScenario instance with the calculated and fetched data.
"""
from rest_framework import viewsets
from .models import LoanScenario
from .serializers import LoanScenarioSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import redirect

# Define constants
API_NINJAS_URL = 'https://api.api-ninjas.com/v1/mortgagecalculator'
API_NINJAS_KEY  = 'uqZZuYWatDs1X8uhEYVBdg==FYGsHMRii31z1jAY' # Ideally this should not be hardcoded.

class LoanScenarioViewSet(viewsets.ModelViewSet):  
    queryset = LoanScenario.objects.all()
    serializer_class = LoanScenarioSerializer
    
    def calculate_loan_details(self, data):
        """
        Calculate loan details based on the provided data and fetch additional information from API Ninjas.
        
        Args:
            data (dict): The validated data from the serializer.
        
        Returns:
            dict: A dictionary containing the calculated loan details.
        
        Raises:
            ValidationError: If there is an error fetching data from API Ninjas.
        """
        # Calculate loan amount        
        loan_amount = data['purchase_price'] - (
            data['down_payment'] if data['down_payment_type'] == 'dollar'
            else data['purchase_price'] * data['down_payment'] / 100
        )
    
        # Calculate term in months
        term_in_months = data['mortgage_term'] if data['term_unit'] == 'months' else data['mortgage_term'] * 12

        # Call API Ninjas
        response = requests.get(
            API_NINJAS_URL,
            params={
                'loan_amount': loan_amount,
                'interest_rate': data['interest_rate'],
                'monthly_term': term_in_months,
            },
            headers={'X-Api-Key': API_NINJAS_KEY},
            timeout=10  # Set a timeout for the request
        )
    
        if response.status_code != 200:
            raise ValidationError(f"Error fetching data from API Ninjas: {response.status_code} - {response.content}")
        
        response_data = response.json()
    
        return {
            'monthly_payment': response_data['monthly_payment']['total'],
            'annual_payment': response_data['annual_payment']['total'],
            'total_payment': response_data['monthly_payment']['total'] * term_in_months,
            'total_interest': response_data['total_interest_paid']
        }

    def perform_update(self, serializer):
        data = serializer.validated_data
        loan_details = self.calculate_loan_details(data)
        serializer.save(**loan_details)

    def perform_create(self, serializer):
        data = serializer.validated_data
        loan_details = self.calculate_loan_details(data)
        serializer.save(**loan_details)
        
# Redirect to loan scenarios        
def redirect_to_loan_scenarios(request):
    return redirect('/api/loan_scenarios/')