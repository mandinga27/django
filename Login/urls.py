from django.urls import path
from Login import views as l_views

urlpatterns = [
    path('', l_views.login, name='login_login'),
    path('logout/', l_views.logout, name='login_logout'),


]
