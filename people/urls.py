
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path( '' , include('peopleApp.urls')),
    path( 'pessoas/' , include('dataApp.urls') ), 
    path('admin/', admin.site.urls),
]
