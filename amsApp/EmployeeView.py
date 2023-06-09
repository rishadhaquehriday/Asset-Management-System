from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404,JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer


# Creating views for Employee   
class EmployeeView(APIView):
    
    def post(self,request):
        data = request.data
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            return JsonResponse('Employee Created Successfully',safe=False)
        return JsonResponse('Failed TO Create Employee',safe=False)
    
    
    def getEmployee(self,pk):
        try:
            employee = Employee.objects.get(employeeId = pk)
            return employee
        except Employee.DoesNotExist():
            return Http404
            
    
    def get(self,pk = None):
        if pk:
            data = self.getEmployee(pk)
            serializer = EmployeeSerializer(data = data)
            return Response(serializer.data)
        else:
            data = Employee.objects.all()
            serializer = EmployeeSerializer(data = data)
            return Response(serializer.data)
        
    
    def put(self,request,pk=None):
        getEmployee = Employee.objects.get(employeeId = pk)
        serializer = EmployeeSerializer(instance = getEmployee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Eployee Updated Successfully',safe=False)
        return JsonResponse('Failed To Update Employee',safe=False)
    
    
    def delete(self,pk=None):
        data = Employee.objects.get(employeeId = pk)
        data.delete()
        return JsonResponse('Employee Deleted Successfully',safe=False)