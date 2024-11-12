from django.urls import path
from materias_app import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path("regMat/",views.regMat,name="regMat"),
    path("selectMat/<codigo>",views.selectMat,name='selectMat'),
    path("editMat/",views.editMat,name='editMat'),
    path("deleteMat/<codigo>",views.deleteMat,name='deleteMat'),
]
