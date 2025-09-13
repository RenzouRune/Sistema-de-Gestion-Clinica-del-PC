from django.shortcuts import render, redirect

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
            request.session['autenticado'] = True
            return redirect('recepcion')  
        else:
            mensaje = 'Usuario o contraseña incorrectos.'
    return render(request, 'login/login.html', {'mensaje': mensaje})

