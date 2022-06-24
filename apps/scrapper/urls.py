from django.urls import path
from . import views 


urlpatterns = [
    path(
        "scrapper/",
        views.ScrapperAPIView.as_view(),
        name="scrapper",
    ),   
]
