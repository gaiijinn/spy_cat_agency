from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("cats", views.CatsModelViewSet)

app_name = "cats"

urlpatterns = [
    path("api/v1/", include(router.urls)),
]