pizzas = [
    {
        'type': "Pepperoni",
        'price': 12.50,
        'sauce': 'red',
        'toppings': ['pepperoni']
    },
    {
        'type': "Cheese",
        'price': 11.25,
        'sauce': 'red',
        'toppings': []
    },
    {
        'type': "Chicken Bacon Ranch",
        'price': 14.10,
        'sauce': 'white',
        'toppings': ['chicken','bacon','ranch']
    },
    {
        'type': "Canadian",
        'price': 13.50,
        'sauce': 'red',
        'toppings': ['sausage','bacon','onion']
    }
]

pizza_order = []

menu = "Please pick one of the following options:"
menu += "\n1) Add pizza to order"
menu += "\n2) Check order for allergn"
menu += "\n3) Print order"
menu += "\n4) Quit"

while True:
    option = int(input(menu))
    if option == 1:
        print("Please select a pizza to order:")
        index = 1
        for pizza in pizzas:
            print(f"\n{index}: {pizza['type']}")
            index += 1
        pizza_choice = int(input("Enter number of pizza to order: "))
        pizza_order.append(pizzas[pizza_choice-1])
    elif option == 2:
        allergen = input("What allergen do you want to check for?")
        allergen_present = []
        for pizza in pizza_order:
            if allergen in pizza['toppings']:
                allergen_present.append(pizza)
            elif allergen == 'tomato' and pizza['sauce'] == 'red':
                allergen_present.append(pizza)
        if allergen_present:
            print("The following pizzas in your order have your allergen:")
            for pizza in allergen_present:
                print(pizza['type'])
        else:
            print("Allergen is not in your order")
    elif option == 3:
        print("Your order:")
        total = 0
        for pizza in pizza_order:
            total += pizza['price']
            print(f"\n{pizza['type']}")
        print(f"\nTotal: {total}")
    elif option == 4:
        quit()
