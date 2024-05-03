pep_pizza_toppings = ['pepperoni']
pep_pizza = {'type' : 'Pepperoni', 'price' : 12.50, 'sauce' : 'red', 'toppings' : pep_pizza_toppings}

che_pizza_toppings = []
che_pizza = {'type' : 'Cheese', 'price' : 11.25, 'sauce' : 'red', 'toppings' : che_pizza_toppings}

cbr_pizza_toppings = ['chicken', 'bacon', 'ranch']
cbr_pizza = {'type' : 'Chicken Bacon Ranch', 'price' : 14.10, 'sauce' : 'white', 'toppings' : cbr_pizza_toppings}

can_pizza_toppings = ['sausage', 'bacon', 'onion']
can_pizza = {'type' : 'Canadian', 'price' : 13.50, 'sauce' : 'red', 'toppings' : can_pizza_toppings}

options = [pep_pizza, che_pizza, cbr_pizza, can_pizza]

current_order = []

prompt = "1. Add pizza to order\n"
prompt+= '2. Check order for allergen\n'
prompt+= '3. Print Order\n'
prompt+= '4. Quit\n'

selection = int(input(prompt))

while selection != 4:
    if selection == 1:
        index = 1
        for pizza in options:
            print(f"\n{index}: {pizza.get('type')}")
            index +=1
        pizza_choice = int(input("Please select a pizza!"))
        current_order.append(options[selection -1])
        print (f"Added {options[selection].get('type')} to your order!\n")
    elif selection == 2:
        allergen = input("What allergen should we check for?")
        for pizza in options:
            if allergen in pizza['Toppings']:
                print(pizza)
    elif selection == 3:
        for pizza in current_order:
            print(pizza)
    elif selection == 4:
        break
    else:
        print("Please enter a valid input")
