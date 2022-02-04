from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):

    STATUS = (
        ("Обробатывается", "Обробатывается"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен"),
    )

    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    clothes = models.ForeignKey(
        ProductCL, on_delete=models.CASCADE, related_name="order_product"
    )
    created_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.clothes.name
