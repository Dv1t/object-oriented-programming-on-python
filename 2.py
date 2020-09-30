class Pizza:
    def __init__(self,souce,filling,dough= "traditional",):
        self.dough = dough
        self.souce = souce,
        self.filling = filling
    def __str__(self):
        return "Pizza "
    def MakePizza(self):
        print(self.__str__() + " is made")
class Pepperoni(Pizza):
    def __init__(self,dough):
        super().__init__("tomato","Pepperoni",dough)
    def __str__(self):
        return super().__str__()+"Pepperoni"
class Barbecue(Pizza):
    def __init__(self,dough):
        super().__init__("BBQ souce","meat and sousages",dough)
    def __str__(self):
        return super().__str__()+"Barbecue"
class Seafood(Pizza):
    def __init__(self,dough):
        super().__init__("tomato","shrimp and mussel",dough)
    def __str__(self):
        return super().__str__()+"Seafood"
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
print("Приятного аппетита!")






