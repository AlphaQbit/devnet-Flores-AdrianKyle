"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: [Flores, Adrian Kyle M.]
"""


pets = []  # starts empty — the user adds pets as the program runs

def display_menu():
    print("1. Add a pet")
    print("2. View all pets")
    print("3. Count available and adopted pets")
    print("4. Find a pet by name")
    print("5. Remove a pet")
    print("6. Exit")
    # print the menu, return the user's choice
    pass

def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    pass

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    pass

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        if choice == 1:
            add_pet(pets)
        elif choice == 2:
            view_pets(pets)
        elif choice == 3:
            count_available_adopted(pets)
        elif choice == 4:
            find_pet(pets)
        elif choice == 5:
            remove_pet(pets)
        elif choice == 6:
            print("Bye!")
            break
        else:
            print("Invalid!")
    pass
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()