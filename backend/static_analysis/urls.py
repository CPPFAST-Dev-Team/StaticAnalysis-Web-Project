from django.urls import path
from .views import InitiateAnalysisView, RetrieveAnalysisResultsView

urlpatterns = [
    path('projects/<int:pk>/analyze/', InitiateAnalysisView.as_view(), name='initiate-analysis'),
    path('projects/<int:pk>/analysis-results/', RetrieveAnalysisResultsView.as_view(), name='analysis-results'),
]