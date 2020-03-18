from django.contrib import admin
from django.urls import path, include
from bookyourcab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookyourcab.urls'))
]
