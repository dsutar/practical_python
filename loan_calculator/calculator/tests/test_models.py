from django.test import TestCase
from calculator.models import LoanScenario

class LoanScenarioModelTest(TestCase):
    def test_can_create_loan_scenario(self):
        loan_scenario = LoanScenario.objects.create(
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
        self.assertTrue(isinstance(loan_scenario, LoanScenario))
        self.assertEqual(loan_scenario.purchase_price, 200000)
        self.assertEqual(loan_scenario.down_payment, 20000)
        self.assertEqual(loan_scenario.down_payment_type, 'dollar')
        self.assertEqual(loan_scenario.mortgage_term, 30)
        self.assertEqual(loan_scenario.term_unit, 'years')
        self.assertEqual(loan_scenario.interest_rate, 3.5)
        self.assertEqual(loan_scenario.monthly_payment, 1000)
        self.assertEqual(loan_scenario.annual_payment, 12000)
        self.assertEqual(loan_scenario.total_payment, 360000)
        self.assertEqual(loan_scenario.total_interest, 160000)
        self.assertIsNotNone(loan_scenario.created_at)