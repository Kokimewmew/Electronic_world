from rest_framework.serializers import ModelSerializer

from electronic.models import Supplier


class SupplierSerializer(ModelSerializer):
    """Сериализотор модели поставщика """
    class Meta:
        model = Supplier
        fields = '__all__'
