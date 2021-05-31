from django.http import Http404
from .serializers import PerformanceReportSerializer, UserSerializer, AdminPerformanceReportSerializer,AdminPerformanceReportListSerializer
from rest_framework import generics
from .models import PerformanceReport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAdminUser
from .permissions import IsEmployee

class PerformanceReportList(APIView):
     permission_classes = [IsEmployee]
     serializer_class = PerformanceReportSerializer
     def get(self, request, *args, **kwargs):
        performancereport = PerformanceReport.objects.filter(employee=self.request.user)
        serializer = PerformanceReportSerializer(performancereport,many = True)
        return Response(serializer.data)

class PerformanceReportCreate(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, format = None):
        performance_reports = PerformanceReport.objects.all()
        serializer = AdminPerformanceReportListSerializer(performance_reports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminPerformanceReportSerializer(data=request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerformanceReportDetail(APIView):
    permission_classes = [IsAdminUser]
    def get_object(self, pk):
        try:
            return PerformanceReport.objects.get(pk=pk)
        except PerformanceReport.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        performance_report = self.get_object(pk)
        serializer = AdminPerformanceReportListSerializer(performance_report)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        perforamnce_report = self.get_object(pk)
        serializer = AdminPerformanceReportSerializer(perforamnce_report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        perforamnce_report = self.get_object(pk)
        perforamnce_report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


