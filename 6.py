from abc import ABC, abstractmethod
from functools import wraps
import datetime
import threading
import time
import asyncio

class InputError(Exception):
    def __str__(self):
        return ("Ошибка ввода")

loop = asyncio.get_event_loop()
#выводит время выполнения декорируемой функции
def write_time_wraper(scenario):
    def write_time(self):
        print(datetime.datetime.now().time())
        return scenario(self)
    return write_time

#абстрактный класс Pizza, содержит основную функциональность,
# но реализовать его нельзя так как нельзя приготовить просто пиццу
class Pizza(ABC):
    def __init__(self,souce,filling,dough= "traditional",):
        self.dough = dough
        self.souce = souce,
        self.filling = filling
    def __str__(self):
        return "Pizza "
    async def MakePizza(self):
        time.sleep(len(self.__str__()))
        print(self.__str__() + " is made")

#Класс миксин который позводяет добавить функциональность позици заказа
class Order_Item_Mixin:
    def __init__(self,cost):
        self.cost = cost
    def get_cost(self):
        return self.cost

#Метакласс
class CheeseAdder(type):
    def AddCheese(cls):
        print("Cheese added to all Pizzas")

    def __call__(self, *args, **kwargs):
        # создаём новый класс как обычно
        cls = type.__call__(self, *args)

        # определяем новый метод hello для каждого из этих классов
        setattr(cls, "AddCheese", self.AddCheese)

        # возвращаем класс
        return cls

#Пицца Пепперони
class Pepperoni(Pizza,Order_Item_Mixin):
    def __init__(self,dough):
        super().__init__("tomato","Pepperoni",dough)
        Order_Item_Mixin.__init__(self,200)
    def __str__(self):
        return super().__str__()+"Pepperoni"
#Пицца Барбекю
class Barbecue(Pizza,Order_Item_Mixin):
    def __init__(self,dough):
        super().__init__("BBQ souce","meat and sousages",dough)
        Order_Item_Mixin.__init__(self,250)
    def __str__(self):
        return super().__str__()+"Barbecue"

#Пицца Дары Моря
class Seafood(Pizza,Order_Item_Mixin):
    def __init__(self,dough):
        super().__init__("tomato","shrimp and mussel",dough)
        Order_Item_Mixin.__init__(self,250)
    def __str__(self):
        return super().__str__()+"Seafood"

#Класс заказа, хранит в себе список заказанных пицц, может его отобразить, приготовить
# и подсчитать стоимость
class Order(metaclass=CheeseAdder):
    def __init__(self):
        self.order_list = list()
    def add_pizza_to_oder(self,pizza):
        if issubclass(pizza.__class__,Pizza):
            self.order_list.append(pizza)
    def display_order(self):
        for item in self.order_list:
            print(item+"\n")
    @write_time_wraper
    def cook_order(self):

        for item in self.order_list:
            loop.run_until_complete(
                asyncio.wait([item.MakePizza()]))

    def calculate_cost(self):
        cost=0
        for item in self.order_list:
            cost+=item.get_cost()
        return "Стоимсоть вашего заказа: "+cost.__str__()


#декоратор, который проверяет правильность ввода
def check_input_decorator(input_method):
    @wraps(input_method)
    def check_input(order,vv0d):
        if (len(vv0d)==1):
            return input_method(order,vv0d)
        else:
            raise InputError
    return check_input

@check_input_decorator
def add_pizza_to_order(order, vv0d):
    if (vv0d == "P"):
        order.add_pizza_to_oder(Pepperoni("thin"))
        return order
    if (vv0d == "B"):
        order.add_pizza_to_oder(Barbecue("traditional"))
        return order
    if (vv0d == "M"):
        order.add_pizza_to_oder(Seafood("thin"))
        return order
    if (vv0d == "0"):
        return order
    raise InputError


#Демонстрация использования созданных классов
my_order = Order()
vvod = ""

while vvod != "0":
    try:
        print('''Введите:
    P для пиццы пепперони, 
    B для пиццы барбекю
    M для пиццы дары моря
    Если вам больше не нужны пицца введите 0''')
        vvod = input()
        my_order = add_pizza_to_order(my_order,vvod)
    except InputError as e:
        print(e.__str__())

my_order.cook_order()
loop.close()
#Используем функцию из метакласса
my_order.AddCheese()

print(my_order.calculate_cost())
print("Приятного аппетита!")






