from django.urls import path
from materias_app import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path("regMat/",views.regMat,name="regMat")
]
