class Pizza:
    """Pizza Class"""
    def __init__(self, name, price, toppings):
        self.name = name
        self.price = price
        self.toppings = toppings
    
    def __str__(self):
        return (f"{self.name} {self.toppings}: ${self.price}")
    
    def has_allergen(self, allergen):
        if allergen in self.toppings:
            return True
        elif allergen == 'tomatoes' or allergen == 'dairy':
            return True
        else:
            return False

    def add_toppings(self, items):
        for item in items:
            if item in self.toppings:
                raise Exception("Item already in pizza")
            self.toppings.append(item)
            self.price += 0.75

class WhitePizza(Pizza):
    def __init__(self, name, price, toppings):
        super().__init__(name, price, toppings)
    
    def has_allergen(self, allergen):
        if allergen in self.toppings:
            return True
        elif allergen == 'dairy':
            return True
        else:
            return False

class PizzaOrder:
    def __init__(self, pizzas):
        self.pizzas = pizzas
    
    def add_pizza(self, pizza):
        if type(pizza) != type(Pizza):
            self.pizzas.append(pizza)
        else:
            raise TypeError("Object passed in is not an instance of Pizza")
    
    def print_order(self):
        index = 1
        for pizza in self.pizzas:
            print(f"{index}. {pizza.name}")
            index += 1
            

    def get_total(self):

    




    