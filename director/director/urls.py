from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('questions.urls')),
    path('admin/', admin.site.urls),
]
