from django.contrib import admin
from electronic.models import Supplier, NetworkElement, Product


class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier', 'debt')
    list_filter = ('city',)

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_debt.short_description = "Очистить задолженность"

    actions = [clear_debt]


admin.site.register(Supplier)
admin.site.register(NetworkElement, NetworkElementAdmin)
admin.site.register(Product)
