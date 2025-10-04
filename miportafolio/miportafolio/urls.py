from django.contrib import admin
from django.urls import path
from proyectos import views
from django.contrib.auth import views as auth_views  # Para login/logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # Pantalla principal (requiere login)
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    
    # Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='proyectos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
