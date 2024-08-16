
from django.urls import path
from .views import EmpSUserRegister, EmpAUserRegister, UserLogin, UserLogout, EmpA_AllUserDetails, EmpS_AllUserDetails
urlpatterns = [

    path('emps_register/',EmpSUserRegister.as_view(), name='emps_register'),
    path('empa_register/',EmpAUserRegister.as_view(), name='empa_register'),
    path('userlogin/',UserLogin.as_view(), name='userlogin'),
    path('userlogout/',UserLogout.as_view(), name='userlogout'),
    path('empa_alluser/',EmpA_AllUserDetails.as_view(), name='empa_alluser'),
    path('emps_alluser/',EmpS_AllUserDetails.as_view(), name='emps_alluser'),
]