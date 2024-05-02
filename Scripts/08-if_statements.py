topping = "mushrooms"
if topping == "mushrooms":
    print("Put mushrooms on")

if topping != "anchovies":
    print("Hold the anchovies!")

age = 20
if (age >= 19):
    print("Can drink in Saskatchewan")

if age>=19 and age<21:
    print("Can drink in Saskatchewan but not in the states")

toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in toppings:
    print("You ordered mushrooms")

if 'pepperoni' in toppings:
    print("You ordered pepperoni")

if 'cheese' not in topping:
    print("Hold the peppers!")

# An empty list is falsy
topping = []
if topping:
    print("You've asked for some toppings")
else:
    print("You haven't ordered any toppings")

print([]==False)


age = 25
if age < 13:
    print("Young child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")