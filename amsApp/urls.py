from django.urls import path
from .CompanyViews import CompanyView
from .EmployeeView import EmployeeView
from .DeviceLogView import DeviceLogView

urlpatterns = [
    
    #company api url
    path('company/',CompanyView.as_view()),
    path('company/<int:pk>/',CompanyView.as_view()),
    
    #employees api url
    path('employees/',EmployeeView.as_view()),
    path('employees/<int:pk>/',EmployeeView.as_view()),
    
    #devicelog api url
    path('log/',DeviceLogView.as_view()),
    path('log/<int:pk>/',DeviceLogView.as_view()),
]