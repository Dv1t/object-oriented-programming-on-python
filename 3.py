from abc import ABC, abstractmethod

#абстрактный класс Pizza, содержит основную функциональность,
# но реализовать его нельзя так как нельзя приготовить просто пиццу
class Pizza(ABC):
    def __init__(self,souce,filling,dough= "traditional",):
        self.dough = dough
        self.souce = souce,
        self.filling = filling
    def __str__(self):
        return "Pizza "
    def MakePizza(self):
        print(self.__str__() + " is made")

#Класс миксин который позводяет добавить функциональность позици заказа
class Order_Item_Mixin:
    def __init__(self,cost):
        self.cost = cost
    def get_cost(self):
        return self.cost

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
class Order:
    def __init__(self):
        self.order_list = list()
    def add_pizza_to_oder(self,pizza):
        if issubclass(pizza.__class__,Pizza):
            self.order_list.append(pizza)
    def display_order(self):
        for item in self.order_list:
            print(item+"\n")
    def cook_order(self):
        for item in self.order_list:
            item.MakePizza()
    def calculate_cost(self):
        cost=0
        for item in self.order_list:
            cost+=item.get_cost()
        return "Стоимсоть вашего заказа: "+cost.__str__()

#Демонстрация использования созданных классов
my_order = Order()
vvod = ""
while vvod != "0":
    print('''Введите:
P для пиццы пепперони, 
B для пиццы барбекю
M для пиццы дары моря
Если вам больше не нужны пицца введите 0''')
    vvod = input()
    if(vvod == "P"):
        my_order.add_pizza_to_oder(Pepperoni("thin"))
    if(vvod == "B"):
        my_order.add_pizza_to_oder(Barbecue("traditional"))
    if(vvod == "M"):
        my_order.add_pizza_to_oder(Seafood("thin"))
my_order.cook_order()
print(my_order.calculate_cost())
print("Приятного аппетита!")

#Не было реализовано множественного наследования (кроме наследования от миксина)
#поскольку в данной области нельзя выделить что то общее наследовавшие свои свойства от двух и более объектов






