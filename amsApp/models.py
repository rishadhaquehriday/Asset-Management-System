from django.db import models


#Company DB Model
class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=100,null=True)
    
    
#Employee DB Model 
class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=100)
    employeeCompany = models.ForeignKey(Company,on_delete=models.CASCADE)
  
    
#Device DB Model   
class Device(models.Model):
    deviceName = models.CharField(max_length=100)
    deviceCompany = models.ForeignKey(Company,on_delete=models.CASCADE)
 
    
#DeviceLog DB Model      
class DeviceLog(models.Model):
    logId = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    checked_out_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=100, null=True, blank=True)

