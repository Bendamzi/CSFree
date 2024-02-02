while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break
    elif user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    else:
        print("Invalid input. Please enter a number or 'quit'.")