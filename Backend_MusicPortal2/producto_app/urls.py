from django.urls import path
from producto_app import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('saveProd/',views.saveProd,name="saveProd"),
    path('editProd/',views.editProd,name="editProd"),
    path('selProd/<id_producto>',views.selProd,name="selProd"),
    path('delProd/<id_producto>',views.delProd,name="delProd"),
]