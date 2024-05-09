from pathlib import Path

 

path = Path("./pi_million_digits.txt")
contents = path.read_text().replace('.', '').replace('\n', '').replace(' ', '')

prompt = "Please select an option:\n"
prompt +="1. Print Digits of Pi\n"
prompt +="2. Find Birthday in Pi\n"
prompt +="3. Quit\n"

option = int(input(prompt))
while(option != 3):
    if option == 1:
        amount = input("Please enter how many digits(0-1,000,000)\n")
        try:
            amount = int(amount)
        except:       
            print (f"{amount} is not a valid number.")
            continue
        
        print(f"First {amount} digits of pi are: ")
        print(f"3.{contents[1:amount]}")
    elif option == 2:
        birthdate = input("Please enter your birthday in the format DD/MM/YYYY\n")
        if birthdate[2:3] != '/' and birthdate[5:6] != '/':
            raise ValueError("Date entered in incorrect format")
        birthdate = birthdate.replace('/', '')
        try:
            int(birthdate)
        except ValueError:
            raise ValueError(f"Could not convert {birthdate} to int")
        try:
            index = contents.index(birthdate)
        except ValueError:
            print(f"Your birthday does not exist in the first million digits of pi.")
            continue
        print(f"Your birthday exists {index} digits into pi.")

    else:
        print('Invalid Entry') 
    option = int(input(prompt))
print('Thank you, goodbye.')
exit