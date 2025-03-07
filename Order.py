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
    def __init__(self, items=None, price = 0.00):
        self.items = items if items else []
        self.price_items = price
        self.data = date.today()
            
    @abstractmethod
    def getOrder(self):
        pass

class ProductOrder(Order):
    def addItems(self):
        self.NameItem = ", ".join(self.items)
        return self.NameItem

    def priceItem(self):
        self.Item_Price = round(sum(self.price_items), 2)
        return self.Item_Price
    
    def getOrder(self):
        return f" Items: {self.NameItem}, price: {self.Item_Price}, data order: {self.data}"

class ServiceOrder(Order):
    def getOrder(self):
        SERVICE_TYPE = "serviceType"
        return f" Items: {ProductOrder.addItems(self)} {SERVICE_TYPE}, price: {ProductOrder.priceItem(self)}, data order: {self.data}"
    
while True:
    try:
        List_Order = [(input("items: ")) for _ in range(int(input("Number items: ")))]
        List_Price = [int(input("price: ")) for _ in List_Order]
        print(ServiceOrder(List_Order, List_Price).getOrder())
    except:
        print("ERROR")
        if input("Write 1:  ") == "1":
            print("Restart")
        else:
            print("Goodbye")
            break
        
