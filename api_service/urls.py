from django.urls import path
from .views import ShortenURLAPIView, RedirectAPIView

urlpatterns = [
    path("shorten/", ShortenURLAPIView.as_view(), name="shorten-url"),
    path("<str:short_code>/", RedirectAPIView.as_view(), name="redirect-url"),
]
