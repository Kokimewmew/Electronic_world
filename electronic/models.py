from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика")
    email = models.EmailField(verbose_name="Электронная почта")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=255, verbose_name="Номер дома")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class NetworkElement(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Электронная почта")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=255, verbose_name="Номер дома")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звено сети'


class Product(models.Model):
    network_element = models.ForeignKey(NetworkElement, on_delete=models.CASCADE, verbose_name="Звено сети")
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
