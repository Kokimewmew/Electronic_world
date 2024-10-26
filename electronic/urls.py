from django.urls import path
from rest_framework.routers import SimpleRouter

from electronic.apps import ElectronicConfig
from electronic.views import SupplierViewSet, SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView

app_name = ElectronicConfig.name

router = SimpleRouter()
router.register("", SupplierViewSet)

urlpatterns = [
    path("<int:pk>/", SupplierRetrieveAPIView.as_view(), name="electronic_retrieve"),
    path("create/", SupplierCreateAPIView.as_view(), name="electronic_create"),
    path("<int:pk>/delete/", SupplierDestroyAPIView.as_view(), name="electronic_delete"),
    path("<int:pk>/update/", SupplierUpdateAPIView.as_view(), name="electronic_update"),

]

urlpatterns += router.urls
