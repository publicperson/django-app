from django.urls import path
from .views import HomPageView, DetailPageView, SearchResultsView

app_name='Personnel'

urlpatterns = [
    path('', HomPageView.as_view(),name='index'),
    path('detail/<int:pk>/', DetailPageView.as_view(),name='detail'),
    path('search/',SearchResultsView.as_view(),name='search_results'),
]