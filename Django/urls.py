"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from pacientes import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home_logged, name='home-logged'),
    url(r'^conta/senha/$', auth_views.PasswordChangeView.as_view(template_name='mudar-senha.html'),
        name='mudar-senha'),
    url(r'^conta/senha/alterada/$', auth_views.PasswordChangeDoneView.as_view(template_name='senha-alterada-sucesso.html'),
    name='password_change_done'),
    url(r'^resetar-senha/$', auth_views.PasswordResetView.as_view(template_name='resetar-senha.html'),
        name='resetar-senha'),
    url(r'^resetar-senha/sucesso$', auth_views.PasswordResetDoneView.as_view(
        template_name='resetar-senha-sucesso.html'), name='password_reset_done'),
    url(r'^resetar-senha-completado/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='senha-resetada-com-sucesso.html'), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='resetar-senha-confirmar.html'), name='password_reset_confirm'),
    url(r'^conta/$', accounts_views.minha_conta, name='conta'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^about/$', views.about, name='about'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^pacientes/(?P<pk>\d+)/$', views.patient_description, name='patient_description'),
]
