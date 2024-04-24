from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('contact-save/', Contact, name='contact_save')
]
