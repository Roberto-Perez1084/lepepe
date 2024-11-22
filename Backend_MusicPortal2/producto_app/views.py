from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def index_view(request):
    productos=Producto.objects.all()
    return render(request,'manageProd.html',{'prod':productos})

def saveProd(request):
    id_producto=request.POST['txtid']
    nom_producto=request.POST['txtnom']
    tipo_producto=request.POST['txttipo']
    cant_producto=request.POST['txtcant']
    metodo_pag=request.POST['txtpag']
    proveedor_prod=request.POST['txtprov']
    id_proveedor=request.POST['txtidprov']

    guardarproducto=Producto.objects.create(id_producto=id_producto,nom_producto=nom_producto,tipo_producto=tipo_producto,cant_producto=cant_producto,metodo_pag=metodo_pag,proveedor_prod=proveedor_prod,id_proveedor=id_proveedor)
    return redirect("/")

def selProd(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request,'editProd.html',{'prod':producto})

def editProd(request):
    id_producto=request.POST['txtid']
    nom_producto=request.POST['txtnom']
    tipo_producto=request.POST['txttipo']
    cant_producto=request.POST['txtcant']
    metodo_pag=request.POST['txtpag']
    proveedor_prod=request.POST['txtprov']
    id_proveedor=request.POST['txtidprod']
    producto=Producto.objects.get(id_producto=id_producto)
    producto.nom_producto=nom_producto
    producto.tipo_producto=tipo_producto
    producto.cant_producto=cant_producto
    producto.metodo_pag=metodo_pag
    producto.proveedor_prod=proveedor_prod
    producto.id_proveedor=id_proveedor
    producto.save()
    return redirect("/")

def delProd(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()

    return redirect("/")