height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        print("$5 Ticket")
    elif age <= 18:
        print("$7 Ticket")
    else:
        print("$12 Ticket")
else:
    print("Too small!")


if height % 2 == 0:
    result = "even"
else:
    result = "odd"

print(result)

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")