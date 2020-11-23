from django.urls import path
from .views import getFormData,saveResponse

urlpatterns =[
    path('getFormData/',getFormData,name='getFormData'),
    path('saveResponse/',saveResponse,name='saveResponse')
]