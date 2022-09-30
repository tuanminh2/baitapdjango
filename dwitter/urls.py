from django.urls import path
from .views import dashboard,profile_list, profile

app_name= "dwitter"
# view name is app_name:viewmethodorclasscustomname
urlpatterns=[
    #method or class from view to url
    path("", dashboard, name="dashboard"),
    path("profile_list",profile_list, name="profile_list"),
    path("profile/<int:pk>",profile, name="profile"),
]