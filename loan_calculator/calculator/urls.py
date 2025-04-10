from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanScenarioViewSet

router = DefaultRouter()
router.register(r'loan_scenarios', LoanScenarioViewSet) #PATH is action_noun format

urlpatterns = [
    path('', include(router.urls)),
]