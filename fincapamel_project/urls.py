from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# --- ESTA LÍNEA ES LA QUE TE FALTABA ---
from django.contrib.auth import views as auth_views 
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- RUTAS PÚBLICAS ---
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('hospedaje/', views.hospedaje, name='hospedaje'),
    path('pasadias/', views.pasadias, name='pasadias'),
    path('eventos/', views.eventos, name='eventos'),

    # --- RUTAS PRIVADAS (Panel de Control) ---
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Nota: Logout ahora requiere POST, pero por simplicidad usaremos esta vista configurada
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('panel/', views.panel, name='panel'),
    
    # Gestión de Posts
    path('panel/nuevo/', views.crear_post, name='crear_post'),
    path('panel/manejar/', views.lista_posts, name='lista_posts'),
    path('panel/editar/<int:id>/', views.editar_post, name='editar_post'),
    path('panel/borrar/<int:id>/', views.borrar_post, name='borrar_post'),
]

# Configuración para ver imágenes en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)