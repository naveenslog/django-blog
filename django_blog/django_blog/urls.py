from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blogapp.urls')),
    path('api/common/', include('common.urls')),
]
