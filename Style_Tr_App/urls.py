from django.urls import path
from . import views

app_name = 'Style_Tr_App'

urlpatterns = [
    path('transfer/', views.transfer, name='transfer'),
    path('downloadimg/', views.download_img, name='download_img'),
]