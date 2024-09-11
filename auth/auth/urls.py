
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
]
