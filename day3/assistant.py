while true:
print("AI ASSISTANT \n Hi, I am your AI assistant. How can I help you today? \n 1)BUY PRODUCT \n 2)GET SUPPORT \n3)TALK TO HUMAN")
choice = input("Enter your choice: ")
if choice == "1":
    print("You have chosen to buy a product. Please visit our website to browse our products.")
elif choice == "2":
    print("You have chosen to get support. Please visit our support page for assistance.")
elif choice == "3":
    print("You have chosen to talk to a human. Please wait while we connect you to a customer service representative.")
elif choice == "4":
    print("succesfully exited")
else:
    print("Invalid choice. Please enter a valid option.")
