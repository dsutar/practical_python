from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch

class LoanScenarioViewSetTest(TestCase):
    """
    Test suite for the LoanScenarioViewSet.

    Classes:
        LoanScenarioViewSetTest: Test case for testing the LoanScenarioViewSet.

    Methods:
        setUp(self):
            Sets up the test client and payloads for valid and invalid loan scenarios.

        test_create_valid_loan_scenario(self, mock_get):
            Tests creating a valid loan scenario and verifies the response.

        test_create_invalid_loan_scenario(self, mock_get):
            Tests creating an invalid loan scenario and verifies the response.

        test_api_ninjas_failure(self, mock_get):
            Tests the scenario where the external API (API Ninjas) fails and verifies the response.
    """
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'purchase_price': 500000,
            'down_payment': 50000,
            'down_payment_type': 'dollar',
            'mortgage_term': 30,
            'term_unit': 'years',
            'interest_rate': 3.5
        }
        self.invalid_payload = {
            'purchase_price': 500000,
            'down_payment': 50000,
            'down_payment_type': 'dollar',
            'mortgage_term': 30,
            'term_unit': 'years',
            'interest_rate': 'invalid_rate'
        }

    @patch('calculator.views.requests.get')
    def test_create_valid_loan_scenario(self, mock_get):
        mock_response = {
            'monthly_payment': {'total': 898},
            'annual_payment': {'total': 10777},
            'total_interest_paid': 123312
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.post(
            '/api/loan_scenarios/',
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['monthly_payment'], mock_response['monthly_payment']['total'])
        self.assertEqual(response.data['annual_payment'], mock_response['annual_payment']['total'])
        self.assertEqual(response.data['total_payment'], mock_response['monthly_payment']['total'] * 360)
        self.assertEqual(response.data['total_interest'], mock_response['total_interest_paid'])

    @patch('calculator.views.requests.get')
    def test_create_invalid_loan_scenario(self, mock_get):
        response = self.client.post(
            '/api/loan_scenarios/',
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('calculator.views.requests.get')
    def test_api_ninjas_failure(self, mock_get):
        mock_get.return_value.status_code = 500

        response = self.client.post(
            '/api/loan_scenarios/',
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)