from django.contrib import admin
from django.urls    import path, include
from mainsite       import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('post/<slug:slug>/', views.showpost),
]
