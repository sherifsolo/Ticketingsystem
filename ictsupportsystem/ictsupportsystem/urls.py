"""
URL configuration for ictsupportsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ticketingsystem import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage),
    path('login/', auth_views.LoginView.as_view(template_name='registration/loginform.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name='registration/passwordresetform.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/passwordresetconfirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'), name='password_reset_complete'),

    path('staff/', views.staffpage, name='dashboard'),
    path('staff/submitform', views.ticketCreationHandler, name='form_submission'),
    path('admin/', admin.site.urls),
]
