from django.shortcuts import render


def login_view(request):
    Usuario = {
        'user': 'inacap',
        'password': 'clinica2025'
    }
    
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == Usuario['user'] and password == Usuario['password']:
            mensaje = '¡Login exitoso!'
            # Aquí puedes redirigir a otra página si lo deseas
        else:
            mensaje = 'Usuario o contraseña incorrectos.'
    return render(request, 'login/login.html', {'mensaje': mensaje})

