print("Give me two numbers, and I'll divide the first by the second")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number:")
    if first_number == 'q':
        break

    answer = int(first_number) / int(second_number)

   #print(f"{first_number} divided by {second_number} is {answer}")
    print("%.2f divided by %.2f is %.2f" % (first_number, second_number, answer))


print("Thank you for using our division calculator")