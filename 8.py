from abc import ABC, abstractmethod
from functools import wraps
import datetime
from tkinter import *
import time

#абстрактный класс Pizza, содержит основную функциональность,
# но реализовать его нельзя так как нельзя приготовить просто пиццу
class Pizza(ABC):
    def __init__(self,souce,filling,dough= "traditional"):
        self.dough = dough
        self.souce = souce,
        self.filling = filling
    def __str__(self):
        return "Pizza "

#Класс миксин который позводяет добавить функциональность позиции заказа
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
    #реализация паттерна Одиночка
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Order, cls).__new__(cls)
        return cls.instance
    def add_pizza_to_oder(self,pizza):
        if issubclass(pizza.__class__,Pizza):
            self.order_list.append(pizza)
    def display_order(self):
        for item in self.order_list:
            print(item+"\n")
    def cook_order(self,cooker):
        for item in self.order_list:
            cooker.cook(item)
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
            print("Ошибка ввода")
            return
    return check_input

@check_input_decorator
def add_pizza_to_order(order, vv0d):
    if (vv0d == "P"):
        order.add_pizza_to_oder(Pepperoni("thin"))
    if (vv0d == "B"):
        order.add_pizza_to_oder(Barbecue("traditional"))
    if (vv0d == "M"):
        order.add_pizza_to_oder(Seafood("thin"))
    return order

class PizzaButton:
    def __init__(self, master, pizza,order):
        self.pizza = pizza
        self.order = order
        self.b = Button(master, width=20, command=self.add_to_order,text = pizza.__str__()+" "+str(pizza.get_cost()))
        self.b.pack()
    #Кнопка реализует паттерн Фасад
    def add_to_order(self):
        self.order.add_pizza_to_oder(self.pizza)
        l['text'] = self.order.calculate_cost()

class CookOrderButton:
    def __init__(self, master, order,cooker):
        self.order = order
        self.cooker = cooker
        self.b = Button(master, width=20, command=self.cook_order,text ="Приготовить заказ")
        self.b.pack()
    def cook_order(self):
        self.order.cook_order(self.cooker)

#Фабрика для создания кнопок
class ButtonFactory():
    def __init__(self,root,order):
        self.root = root
        self.order = order

    def CreateButton(self,pizza):
        return PizzaButton(self.root,pizza,self.order)

class CookerVasya():
    def cook(self,pizza):
        o["text"] = pizza.__str__()+" готовится Васей"

class CookerPetya():
    def cook(self,pizza):
        o["text"] = pizza.__str__()+" готовится Петей"

#Демонстрация использования созданных классов
my_order = Order()
#инициализация главного окна
root = Tk()
#строка для вывода
l=Label(text="")
l.pack()
#создание кнопок с помощью фабрики
buttonMaker = ButtonFactory(root,Order())
buttonMaker.CreateButton(Pepperoni("thin"))
buttonMaker.CreateButton(Barbecue("traditional"))
buttonMaker.CreateButton(Seafood("thin"))

CookOrderButton(root,my_order,CookerVasya())

CookOrderButton(root,my_order,CookerPetya())
o=Label(text="")
o.pack()

root.mainloop()







