from django.shortcuts import render,redirect
from .models import Cliente

# Create your views here.

def index_view(request):
    clientes=Cliente.objects.all()
    return render(request,'manageCli.html',{'clt':clientes})

def saveCli(request):
    id_cliente=request.POST['txtid']
    nom_cliente=request.POST['txtnombre']
    apelli_cliente=request.POST['txtapellido']
    edad_cliente=request.POST['numedad']
    tel_cliente=request.POST['numtel']
    email_cliente=request.POST['txtemail']
    fech_reg=request.POST['datereg']

    guardarcliente=Cliente.objects.create(id_cliente=id_cliente,nom_cliente=nom_cliente,apelli_cliente=apelli_cliente,edad_cliente=edad_cliente,tel_cliente=tel_cliente,email_cliente=email_cliente,fech_reg=fech_reg)
    return redirect('/')

def selCli(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,'editCli.html',{'clt':cliente})

def editCli(request):
    id_cliente=request.POST['txtid']
    nom_cliente=request.POST['txtnombre']
    apelli_cliente=request.POST['txtapellido']
    edad_cliente=request.POST['numedad']
    tel_cliente=request.POST['numtel']
    email_cliente=request.POST['txtemail']
    fech_reg=request.POST['datereg']
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nom_cliente=nom_cliente
    cliente.apelli_cliente=apelli_cliente
    cliente.edad_cliente=edad_cliente
    cliente.tel_cliente=tel_cliente
    cliente.email_cliente=email_cliente
    cliente.fech_reg=fech_reg
    cliente.save()
    return redirect('/')

def delCli(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()

    return redirect("/")