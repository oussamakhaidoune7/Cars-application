#  Definition of the car list
cars = ["Mercedes-Benz","BMW", "VolksWagen", "Audi", "Porsche", "Opel","Maybach","Ford","Dodge","Jeep"]

# Function to display available cars
def afficher_voitures():
    if cars:
        print("\navailable cars :")
        for voiture in cars:
            print(f"- {voiture}")
    else:
        print("\nNo car available.")

# Function to add a car to the list
def ajouter_voiture():
    voiture = input("Enter the name of the car to add : ")
    cars.append(voiture)
    print(f"{voiture} has been added to the list.")

# Function to search for a car in the list
def rechercher_voiture():
    voiture = input("Enter the name of the car to search for : ")
    if voiture in cars:
        print(f"{voiture} is available in the list.")
    else:
        print(f"{voiture} is not available in the list.")

# Function to remove a car from the list
def supprimer_voiture():
    voiture = input("Enter the name of the car to delete : ")
    if voiture in cars:
        cars.remove(voiture)
        print(f"{voiture} has been removed from the list.")
    else:
        print(f"{voiture} does not exist in the list.")

# main menu of the application
def menu():
    while True:
        print("\nMenu:")
        print("1 - Show available cars")
        print("2 - add a car")
        print("3 - Search a car")
        print("4 - Delete a car")
        print("5 - leave")
        
        choice = input("choose an option : ")
        
        if choice == "1":
            afficher_voitures()
        elif choice == "2":
            ajouter_voiture()
        elif choice == "3":
            rechercher_voiture()
        elif choice == "4":
            supprimer_voiture()
        elif choice == "5":
            print("goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# application execution
menu()