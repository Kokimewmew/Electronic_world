from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwner, IsModer
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'city', 'country']
    ordering_fields = ['name', 'created_at']

    # Фильтр по стране
    filterset_fields = ['country']

    # Запрет изменения поля "debt" через API
    def perform_update(self, serializer):
        # Копируем все поля, кроме debt
        initial_data = serializer.validated_data.copy()
        del initial_data['debt']
        serializer.save(data=initial_data)


class SupplierCreateAPIView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #permission_classes = (~IsModer, IsAuthenticated)


class SupplierRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #permission_classes = (IsAuthenticated, IsOwner | IsModer)


class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #permission_classes = (IsAuthenticated, IsOwner | IsModer)


class SupplierDestroyAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #permission_classes = (IsAuthenticated, IsOwner)
