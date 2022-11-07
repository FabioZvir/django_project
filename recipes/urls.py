from django.urls import path
from django.contrib import admin
from recipes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
