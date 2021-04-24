from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

# See https://docs.djangoproject.com/en/3.2/topics/http/urls/

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("users/", include("orchard.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("api/", include("orchard.api_router")),
    path("auth-token/", obtain_auth_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
