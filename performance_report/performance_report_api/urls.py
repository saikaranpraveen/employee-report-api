from django.urls import path
from .views import UserCreate, LoginView, PerformanceReportList, PerformanceReportCreate,PerformanceReportDetail

urlpatterns = [
    path("register/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("performancereportlist/", PerformanceReportList.as_view(), name= "list_all"),
    path("viewallreports/", PerformanceReportCreate.as_view(), name= "create_report"),
    path("createreportdetail/<int:pk>", PerformanceReportDetail.as_view(), name= "create_report")
]