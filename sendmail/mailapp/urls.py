from django.contrib import admin
from django.urls import path
from .views import home, sendmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sendmail', sendmail, name='sendmail'),
]
