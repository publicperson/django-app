from django.urls import path
from .views import HomePageView, DetailPageView,FormPageView

app_name = 'jobs'

urlpatterns = [
    path('',HomePageView.as_view(),name='joblist'),
    path('jobdetails/<int:pk>/',DetailPageView.as_view(),name='jobdetail'),
    path('jobform/', FormPageView.as_view(),name = 'jobform')
]
