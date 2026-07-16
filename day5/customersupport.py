def greet_customer():
    print("Hello! Welcome to our support center.\n")


def check_issue_type():
    while True:
        print("What issue are you facing?")
        print("1. Refund")
        print("2. Technical Issue")
        print("3. Order Status")

        choice = input("Enter your choice (1-3): ")

        if choice == "1" or choice == "2" or choice == "3":
            return choice

        print("\nInvalid option! Please choose 1, 2, or 3.\n")


def generate_response(choice):
    if choice == "1":
        print("\nI will help you with your refund.")

    elif choice == "2":
        print("\nI will connect you to technical support.")

    elif choice == "3":
        print("\nI will check your order status.")


def goodbye_customer():
    print("\nThank you for contacting us.")
    print("Have a great day!")


# Main Program
greet_customer()

user_choice = check_issue_type()

generate_response(user_choice)

goodbye_customer()