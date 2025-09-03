from django.urls import path
from . import views


urlpatterns = [
   path("",views.homepage,name="homepage"),
#    path("auth/signup/", SignUpView.as_view(), name="signup"),
]
