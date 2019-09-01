from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special')
]
