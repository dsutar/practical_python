from rest_framework.test import APITestCase
from calculator.serializers import LoanScenarioSerializer
from calculator.models import LoanScenario


class LoanScenarioSerializerTest(APITestCase):
    def setUp(self):
        self.loan_scenario = LoanScenario.objects.create(
            purchase_price=200000,
            down_payment=20000,
            down_payment_type='dollar',
            mortgage_term=30,
            term_unit='years',
            interest_rate=3.5,
            monthly_payment=1000,
            annual_payment=12000,
            total_payment=360000,
            total_interest=160000
        )
        self.serializer = LoanScenarioSerializer(instance=self.loan_scenario)
        
        
    def test_contails_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'purchase_price', 'down_payment', 'down_payment_type', 'mortgage_term', 'term_unit', 'interest_rate', 'monthly_payment', 'annual_payment', 'total_payment', 'total_interest', 'created_at']))    
        
    def test_monthly_payment_field(self):
        self.assertEqual(self.serializer.data['monthly_payment'], self.loan_scenario.monthly_payment)
        
    def test_annual_payment_field(self):
        self.assertEqual(self.serializer.data['annual_payment'], self.loan_scenario.annual_payment)