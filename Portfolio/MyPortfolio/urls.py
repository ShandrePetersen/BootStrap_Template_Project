from django.urls import paths
from .views import IndexView

app_name = "MyPortfolio"

urlpatterns = [
    paths("", IndexView.as_view(), name="index"),
]