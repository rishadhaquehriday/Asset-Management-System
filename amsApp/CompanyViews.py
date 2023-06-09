from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404,JsonResponse
from .models import Company
from .serializers import CompanySerializer


# Creating views for company
class CompanyView(APIView):
    
    def post(self,request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Company Created Successfully',safe=False)
        return JsonResponse('Failed To Create Successfully', safe=False)
    
    
    def get_company(self,pk):
        try:
            company = Company.objects.get(companyId = pk)
            return company
        except Company.DoesNotExist():
            raise Http404
    
    
    def get(self,request,pk=None):
        if pk:
            data = self.get_company(pk)
            serializer = CompanySerializer(data=data)
            return Response(serializer.data)
        else:
            data = Company.objects.all()
            serializer = CompanySerializer(data = data)
            return Response(serializer.data)
        
        
    def put(self,request,pk = None):
        companyToUpdate = Company.objects.get(companyId = pk)
        serializer = CompanySerializer(instance = companyToUpdate,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Company Updated Successfully',safe=False)
        return JsonResponse('Failed To Update Company')
    
    
    def delete(self,request,pk = None):
        data = Company.objects.get(companyId = pk)
        data.delete()
        return JsonResponse('Company Deleted Successfully',safe = False)
    
    
 
    
    
        
        
        
        
                
        
            
        

