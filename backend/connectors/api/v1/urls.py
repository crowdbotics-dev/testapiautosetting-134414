from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134414ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134414", Testconnectors134414ViewSet, basename="testconnectors134414"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
