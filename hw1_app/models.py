from django.db import models


# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    reg_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Client: {self.name} {self.phone}'

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Items(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Item: {self.title} {self.price} {self.quantity} {self.date_created}'


# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)
    total = models.DecimalField(max_digits=20, decimal_places=10)
    date_order = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order: {self.client} {self.items} {self.total} {self.date_order}'

