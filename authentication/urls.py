from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', log_in, name='login'),
    path ('signup/', sign_up, name='signup'),
    path('logout/', log_out, name='logout'),
]