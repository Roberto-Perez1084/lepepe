from django.urls import path
from cliente_app import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('saveCli/',views.saveCli,name="saveCli"),
    path('editCli/',views.editCli,name="editCli"),
    path('selCli/<id_cliente>',views.selCli,name="selCli"),
    path('delCli/<id_cliente>',views.delCli,name="delCli"),
]