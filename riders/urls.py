from django.urls import path
from riders import views

app_name = 'riders'

urlpatterns = [
    path('', views.riders, name="riders"),
    # path('detail/<str:pk>', views.rider_detail, name="rider-detail"),
    path('plate_req/', views.plate_req, name="plate-req"),
    path('importcsv/', views.import_csv, name="importcsv"),
    path('validation_licence/', views.validation_licence, name="validation-licence"),
]
