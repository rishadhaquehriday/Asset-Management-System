from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import DeviceLog
from .serializers import DeviceLogSerializer


# Creating views for device log
class DeviceLogView(APIView):
    
    def post(self,request):
        data = request.data
        serializer = DeviceLogSerializer(data = data)
        if serializer.is_valid():
            return JsonResponse('Device Added Successfully',safe = False)
        return JsonResponse('Device Added Successfully',safe = False)
    
    
    def get(self):
            data = self.objects.all()
            serializer = DeviceLogSerializer(data = data)
            return Response(serializer.data)
        
        
    def put(self,request,pk = None):
        identifyLog = DeviceLog.objects.get(logId = pk)
        serializer = DeviceLogSerializer(instance = identifyLog,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Log Updated Successfully',safe=False)
        return JsonResponse('Failed TO Update Log',safe=False)