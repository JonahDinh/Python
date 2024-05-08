print("Give me two numbers, and I'll divide the first by the second")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number:")
    if first_number == 'q':
        break
    second_number = input("Second Number:")
    if first_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        continue
    except ValueError:
        print("Please enter only numbers")
        continue
    except Exception as e:
        print("Some random error occured")
        print(e)
        continue

   #print(f"{first_number} divided by {second_number} is {answer}")
    print("%.2s divided by %.2s is %.2f" % (first_number, second_number, answer))


print("Thank you for using our division calculator")