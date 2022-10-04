from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("administrator.urls")),
    path("", include("homepage.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("users.urls")),
    path("", include("promotions.urls")),
    path("api/v1/", include("apiv1.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
