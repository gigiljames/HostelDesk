from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('HostelDesk/',include('HostelDesk.urls')),
    path('admin/', admin.site.urls),
]
