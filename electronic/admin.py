from django.contrib import admin
from electronic.models import Supplier, NetworkElement, Product


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_debt.short_description = "Очистить задолженность"

    actions = [clear_debt]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('network_element', 'name', 'model', 'release_date',)
