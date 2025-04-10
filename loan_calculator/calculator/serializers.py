from rest_framework import serializers
from calculator.models import LoanScenario

class LoanScenarioSerializer(serializers.ModelSerializer):
    """
    Serializer for the LoanScenario model.

    This serializer handles the conversion of LoanScenario instances to and from JSON format.
    It includes read-only fields for monthly_payment, annual_payment, total_payment, and total_interest.
    Custom validation is provided for the interest_rate and down_payment fields.
    """
    monthly_payment = serializers.FloatField(read_only=True)
    annual_payment = serializers.FloatField(read_only=True)
    total_payment = serializers.FloatField(read_only=True)
    total_interest = serializers.FloatField(read_only=True)
    
    class Meta:
        model = LoanScenario
        fields = ['purchase_price', 'down_payment', 'mortgage_term', 'interest_rate', 'monthly_payment', 'annual_payment', 'total_payment', 'total_interest']
        
        def validate_interest_rate(self, value):
            """
            Validate the interest rate to ensure it is between 0 and 100.
            """
            if value < 0 or value > 100:
                raise serializers.ValidationError('Interest rate must be between 0 and 100')
            return value
        
        def validate(self, data):
            """
            Validate the down payment when the type is 'percent' to ensure it is between 0 and 100.
            """
            if data['down_payment_type'] == 'percent' and (data['down_payment'] < 0 or data['down_payment'] > 100):
                raise serializers.ValidationError('Down payment must be between 0 and 100')
            return data
        