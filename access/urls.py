from django.contrib.auth import views as auth_views
from django.urls import path
from galleria import settings

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='access/login.html'), name='access_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='access_logout'),
]
