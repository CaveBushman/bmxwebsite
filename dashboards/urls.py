from django.urls import path
from dashboards import views

app_name = 'dashboards'

urlpatterns = [
    path('', views.dashboards, name="dashboards"),
    #path('detail/<str:pk>', views.club_detail, name="club-detail")
]
