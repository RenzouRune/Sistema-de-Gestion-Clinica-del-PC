from django.shortcuts import render, redirect
from .models import usuarios, roles

def login_view(request):
    mensaje = ''
    # Inicializa la variable de sesión solo si no existe
    if 'autenticado' not in request.session:
        request.session['autenticado'] = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = usuarios.objects.filter(nombre=username, contraseña=password).first()
        if user:
            request.session['autenticado'] = True
            request.session['user'] = user.nombre
            request.session['rol'] = user.rol
            return redirect('recepcion')
        else:
            mensaje = 'Usuario o contraseña incorrectos.'
            request.session['autenticado'] = False  # Asegura que siga en False si falla

    return render(request, 'login/login.html', {'mensaje': mensaje})

def register_view(request):
    mensaje = ''
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        rol = request.POST.get('rol')
        if usuarios.objects.filter(nombre=nombre).exists():
            mensaje = 'El usuario ya existe.'
        else:
            usuarios.objects.create(nombre=nombre, contraseña=contraseña, rol=rol)
            return redirect('login')
    roles_list = roles.objects.all()
    return render(request, 'login/register.html', {'roles': roles_list, 'mensaje': mensaje})

def create_role_view(request):
    mensaje = ''
    if request.method == 'POST':
        nombre_rol = request.POST.get('nombre_rol')
        descripcion = request.POST.get('descripcion')
        if roles.objects.filter(nombre_rol=nombre_rol).exists():
            mensaje = 'El rol ya existe.'
        else:
            roles.objects.create(nombre_rol=nombre_rol, descripcion=descripcion)
            return redirect('register')
    return render(request, 'login/create_role.html', {'mensaje': mensaje})

def logout_view(request):
    if request.method == 'POST':
        request.session['autenticado'] = False
        request.session.pop('user', None)
        request.session.pop('rol', None)
        return redirect('/')
    return render(request, 'login/logout.html')
