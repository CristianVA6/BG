from django.shortcuts import render
import pyqrcode as QRCODE

# Create your views here.
def home(request):
    return render(request,'registro.html')

def prueba(request):
    Datos = []
    if request.method == 'GET':
        Datos = [request.GET.get('Nombre'),request.GET.get('Matricula'),request.GET.get('Carrera'),request.GET.get('Semestre'),
        request.GET.get('CM')]
    CrearQR = QRCODE.create(",".join(Datos))
    CrearQR.png("../BigDataRegister/static/imagenes/1.png",scale=6)    
    return render(request,'codigoQR.html')