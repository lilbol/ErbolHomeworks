from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    date_creat = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return  self.name


class Order(models.Model):
    STATUS = (
        ('Обробатывается', 'Обробатывается'),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='order_product')
    created_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.product.name