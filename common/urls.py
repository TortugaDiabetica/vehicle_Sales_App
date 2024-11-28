from django.urls import path, include
from .views import HomePageView, AboutPageView, ContactPageView
from django.conf import settings
from django.conf.urls.static import static

app_name = "common"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
