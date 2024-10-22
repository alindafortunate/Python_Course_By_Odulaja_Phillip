# A system that has many if statements.
question = input('Are you hungry? Answer is either "Yes" or "No" ')

if question == "Yes":
    print("Go to the Grocery store.")

    chocolate_price = int(input("How much does the chocolate cost? "))
    if chocolate_price <= 1:
        print("Buy 3")
    else:
        print("Buy 1")
elif question == "No":
    print("Stay at home")
    fortnite = input("Do you want to play a fortnite? ")
    if fortnite == "Yes":
        print("See you next week.")
    elif fortnite == "No":
        print("Go back to study.")
        favourite_subject = input("What is your favorite subject? ")
        if favourite_subject == "Computer Science":
            print("That's my favorite subject")
        else:
            print('We have nothing in common bye.')    
    else:
        print("Invalid response.")
else:
    print("Invalid response")
