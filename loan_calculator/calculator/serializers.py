from rest_framework import serializers
from .models import LoanScenario

class LoanScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanScenario
        fields = [
            "id",
            "loan_amount",
            "interest_rate",
            "loan_term",
            "monthly_payment",
            "annual_payment",
            "total_payment",
            "created_at"
        ]

    def validate(self, data):
        if data["loan_amount"] <= 0:
            raise serializers.ValidationError("Loan amount must be positive.")
        if data["interest_rate"] <= 0 or data["interest_rate"] > 100:
            raise serializers.ValidationError("Interest rate must be between 0 and 100.")
        if data["loan_term"] <= 0:
            raise serializers.ValidationError("Loan term must be positive.")
        return data
