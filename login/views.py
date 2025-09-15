from django.shortcuts import render, redirect
autenticado = False

def login_view(request):
    autenticado = False
    Usuario = {
        'user': 'inacap',
        'password': 'clinica2025'
    }
    mensaje = ''
    # Inicializa la variable de sesión solo si no existe
    if 'autenticado' not in request.session:
        request.session['autenticado'] = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == Usuario['user'] and password == Usuario['password']:
            request.session['autenticado'] = True
            return redirect('recepcion')
        else:
            mensaje = 'Usuario o contraseña incorrectos.'
            request.session['autenticado'] = False  # Asegura que siga en False si falla

    return render(request, 'login/login.html', {'mensaje': mensaje})

