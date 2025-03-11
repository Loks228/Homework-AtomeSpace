#Реалізувати ієрархію класів Order, ProductOrder, ServiceOrder.
#Усі об'єкти типу Order повинні містити властивості:
#price (сума замовлення з точністю до двох знаків після коми),
#name,
#масив items рядкового типу (у вигляді імен),
#orderDate (дата створення замовлення).
#Кінцевий користувач не повинен мати можливості створювати об'єкт Order, але повинен мати можливість безперешкодно створювати ProductOrder та ServiceOrder.
#ServiceOrder повинен містити властивість рядкового типу serviceType.
#Усі об'єкти типу Order повинні надавати наступні публічні методи:
#getOrder(): String — повертає інформацію про замовлення у вигляді рядка у форматі:
#"%ORDER_NAME%-%PRICE%-%ORDER_DATE%"
#для об'єкта типу ServiceOrder: "%ORDER_NAME%-%SERVICE_TYPE%-%PRICE%-%ORDER_DATE%".
#addItem(String item, Number itemPrice): void — додає новий item до масиву items та оновлює властивість price об'єкта Order.
#Усі поля та інші службові методи не повинні бути доступні для користувача класів Order ззовні.

from abc import ABC, abstractmethod
from datetime import date

class Order(ABC):

    def __init__(self, items=None, price = 0.00, percent = 0):
        self.items = items if items else []
        if type(self.items) == list:
            self.items = ", ".join(self.items)
        self.price_items = price
        self.data = date.today()
        self.percent = percent

    @abstractmethod
    def getOrder(self):
        pass


class ProductOrder(Order):
    def addItems(self, price):
        if type(price) == list:
            self.price_items += sum(price)
        else:
            self.price_items += price
        return self.price_items

    def getOrder(self):
        return f" Items: {self.items} , price: {self.price_items + (self.price_items * self.percent) / 100}, data order: {self.data}"

class ServiceOrder(Order):
    def addItems(self, price):
        if type(price) == list:
            self.price_items += sum(price)
        else:
            self.price_items += price
        return self.price_items
    
    def getOrder(self):
        SERVICE_TYPE = "serviceType "
        return f" Items: {self.items} {SERVICE_TYPE}: {self.percent}%, price: {self.price_items + (self.price_items * self.percent) / 100}, data order: {self.data}"
    
while True:
        try:
            List_Order = [(input("items: ")) for _ in range(int(input("Number items: ")))]
            List_Price = [int(input("price: ")) for _ in List_Order]
            client = ProductOrder(List_Order)
            client.addItems(List_Price)
            print(client.getOrder())
            
            ServicePercent = int(input("percent: "))
            ServiceClient = ServiceOrder(List_Order, 0.00, ServicePercent)
            ServiceClient.addItems(10)
            ServiceClient.addItems(50)
            print(ServiceClient.getOrder())
        except:
            print("ERROR")
            if input("Write 1:  ") == "1":
                print("Restart")
            else:
                print("Goodbye")
                break
        
