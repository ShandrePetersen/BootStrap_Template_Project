from django.urls import paths
from .views import IndexView


urlpatterns = [
    paths("", IndexView.as_view(), name="index"),
]