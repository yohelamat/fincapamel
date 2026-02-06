from .models import ArticuloBlog, Servicio
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogForm

def index(request):
    # Traemos los servicios desde la base de datos para mostrarlos en el inicio
    servicios = Servicio.objects.all()
    return render(request, 'index.html', {'servicios': servicios})

def blog(request):
    # Traemos todos los artículos del blog
    posts = ArticuloBlog.objects.all()
    return render(request, 'blog.html', {'posts': posts})

# Vistas estáticas para las páginas internas
def hospedaje(request):
    return render(request, 'hospedaje.html')

def pasadias(request):
    return render(request, 'pasadias.html')

def eventos(request):
    return render(request, 'eventos.html')

@login_required(login_url='/admin/login/') # Si no está logueado, lo manda al login del admin
def crear_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog') # Al guardar, te lleva al blog para ver la noticia
    else:
        form = BlogForm()
    
    return render(request, 'crear_post.html', {'form': form})

# 1. EL PANEL PRINCIPAL (MENÚ)
@login_required
def panel(request):
    return render(request, 'panel.html')

# 2. LISTA PARA MANEJAR POSTS
@login_required
def lista_posts(request):
    posts = ArticuloBlog.objects.all().order_by('-fecha_publicacion')
    return render(request, 'lista_posts.html', {'posts': posts})

# 3. EDITAR UN POST
@login_required
def editar_post(request, id):
    post = get_object_or_404(ArticuloBlog, id=id) 
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = BlogForm(instance=post)
    
    # Usamos el HTML específico para EDITAR (Nuevo)
    return render(request, 'editar_post.html', {'form': form, 'post': post})

@login_required
def borrar_post(request, id):
    post = get_object_or_404(ArticuloBlog, id=id)
    
    if request.method == 'POST':
        # Si confirmaron (dieron clic al botón rojo del formulario), se borra
        post.delete()
        return redirect('lista_posts')
        
    # Si solo entraron al link, mostramos la página de confirmación (Nuevo)
    return render(request, 'borrar_post.html', {'post': post})

# 5. CREAR POST (Ya la tenías, solo confirma que redirija a 'panel' o 'blog')
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog') 
    else:
        form = BlogForm()
    return render(request, 'crear_post.html', {'form': form})