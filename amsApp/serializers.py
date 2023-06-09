from rest_framework import serializers
from .models import Company,Employee,Device,DeviceLog	


#Company Serializer Definition
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('companyId','companyName')
        
#Employee Serializer Definition
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeId','employeeName','employeeCompany')
       
#Device Serializer Definition        
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('deviceName','deviceCompany')
        
#Device Log Serializer Definition
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = ('logId','device','checked_out_by','checked_out_at','returned_at','condition')