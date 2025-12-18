'''
Shoe Inventory Management System

This program allows users to manage an inventory of shoes.
Users can read shoe data from a file, add new shoes, view all shoes,
restock shoes, search for shoes by code, calculate the value of each item,
and identify the shoe with the highest quantity.

All data is stored in 'inventory.txt' file.
'''

import os

# ========== Class Definition ==========


class Shoe:

    # Shoe class to represent a shoe in the inventory
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Returns the cost of a given shoe
    def get_cost(self):
        return self.cost

    # Returns the quantity of a given shoe
    def get_quantity(self):
        return self.quantity

    # Returns a shoe in the form of a string
    def __str__(self):
        shoe_string = f"Shoe(country: {self.country}, code: {self.code}, product: {self.product}, cost: {self.cost}, quantity: {self.quantity})"
        return shoe_string


# =========== Shoe List ===========
shoe_list = []


# ============== Functions ==============
def read_shoes_data():
    '''
    This function will read the shoe data from the inventory.txt
    and add the data to a list.

    Parameters:
    None

    Returns:
    None
    '''
    # Ensure the inventory file exists
    if not os.path.exists('inventory.txt'):

        with open('inventory.txt', 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            pass

    else:
        with open('inventory.txt', 'r') as file:
            next(file)

            # Take each line in the file and create a shoe object
            # Then append this object into the shoe list
            for line in file:

                try:
                    country, code, product, cost, quantity = line.strip().split(',')
                    shoe = Shoe(country, code, product,
                                float(cost), int(quantity))
                    shoe_list.append(shoe)

                except ValueError as e:
                    print(f"Error reading line: {line.strip()}. Error: {e}")


def capture_shoes():
    '''
    This function allows the user to add a new shoe to the inventory.
    It then adds this new shoe to the list and then the list is updated
    in the inventory.txt file.

    Parameters:
    None

    Returns:
    None
    '''
    shoe_country = input("Enter the shoe's country of origin: ")

    while True:
        temp_shoe_code = input("Enter a 5 digit unique code for the shoe: ")

        # Make sure the shoe code is 5 digits and numeric
        if len(temp_shoe_code) == 5 and temp_shoe_code.isdigit():
            break

        else:
            print("Invalid input. Please enter a 5 digit numeric code.")

    shoe_code = "SKU" + temp_shoe_code

    # Make sure the shoe is new by checking the code against existing codes
    while shoe_code not in [shoe.code for shoe in shoe_list]:
        shoe_product = input("Enter the name of the shoe: ")

        while True:

            try:

                shoe_cost = float(input("Enter the cost of the shoe: "))

                if shoe_cost < 0:
                    print("Please enter a positive value for cost.")
                    continue

                break

            except ValueError:
                print("Invalid input. Please enter a numeric value for cost.")

        while True:

            try:

                shoe_quantity = int(input("Enter the quantity of the shoe: "))
                if shoe_quantity < 0:
                    print("Please enter a positive integer for quantity.")
                    continue

                break

            except ValueError:
                print("Invalid input. Please enter an integer value for quantity.")

        # Create a new shoe object and add it to the list and file
        new_shoe = Shoe(shoe_country, shoe_code, shoe_product,
                        shoe_cost, shoe_quantity)
        shoe_list.append(new_shoe)

        with open('inventory.txt', 'a') as file:
            file.write(
                f"\n{shoe_country},{shoe_code},{shoe_product},{shoe_cost},{shoe_quantity}")

        print("New shoe added successfully.")
        break

    else:
        print("Shoe code already exists. Please enter a unique code.")


def view_all():
    '''
    Prints all shoes in the inventory.

    Parameters:
    None

    Returns:
    None
    '''
    for shoe in shoe_list:
        print(shoe.__str__())


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity
    and ask the user if they want to restock it. If so, the quantity
    will be updated both in the object and in the inventory.txt file.

    Parameters:
    None

    Returns:
    None
    '''
    for shoe in shoe_list:

        # Finds the shoe with the lowest quantity
        if shoe.get_quantity() == min(shoe.get_quantity() for shoe in shoe_list):
            print(
                f"The shoe with the lowest quantity is: {shoe.product} (Code: {shoe.code}) with quantity {shoe.quantity}.")
            restock_decision = input(
                "Do you want to restock this shoe? (Yes / No): ").strip().lower()

            if restock_decision == 'yes':

                while True:

                    try:
                        additional_quantity = int(
                            input("Enter the quantity to add: "))

                        # The additional stock must be a positive integer
                        if additional_quantity < 0:
                            print("Please enter a positive integer.")
                            continue

                        shoe.quantity += additional_quantity

                        with open('inventory.txt', 'w') as file:
                            file.write("Country,Code,Product,Cost,Quantity\n")

                            for s in shoe_list:
                                file.write(
                                    f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n")

                        print(
                            f"Updated quantity for {shoe.product} is now {shoe.quantity}.")
                        break

                    except ValueError:
                        print("Invalid input. Please enter an integer value.")

            elif restock_decision == 'no':
                print("No changes made to the stock.")
                break

            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")


def search_shoe():
    '''
    This function will search for a shoe from the list
    and print its details.

    Parameters:
    None

    Returns:
    None
    '''
    while True:
        shoe_choice = input("Enter a 5 digit unique code for the shoe: ")

        # Make sure the shoe code is 5 digits and numeric
        if len(shoe_choice) == 5 and shoe_choice.isdigit():
            break

        else:
            print("Invalid input. Please enter a 5 digit numeric code.")

    shoe_search = "SKU" + shoe_choice

    for shoe in shoe_list:

        if shoe.code == shoe_search:
            print(shoe.__str__())
            break

    else:
        print("Shoe not found in inventory.")


def value_per_item():
    '''
    This fuction will calculate the total value for each item.
    It will display all shoes with their respective total values,
    in addition to the total value of all shoe stock.

    Parameters:
    None

    Returns:
    None
    '''
    total_value = 0

    for shoe in shoe_list:
        shoe_value = shoe.get_cost() * shoe.get_quantity()
        total_value += shoe_value
        print(
            f"The total value for {shoe.product} (Code: {shoe.code}) is: {shoe_value:.2f}")

    print(f"The overall total value of all shoes is: {total_value:.2f}")


def highest_qty():
    '''
    This function will determine the shoe with the highest quantity
    and print this shoe as being for sale.

    Parameters:
    None

    Returns:
    None
    '''
    for shoe in shoe_list:

        if shoe.get_quantity() == max(shoe.get_quantity() for shoe in shoe_list):
            print(
                f"The shoe with the highest quantity is: {shoe.product} (Code: {shoe.code}) with quantity {shoe.quantity}. This shoe is now for sale!")


# ============= Main Menu =============
read_shoes_data()

while True:
    print("Shoe Inventory Management System\n".title())
    print("1. Capture New Shoe\n"
          "2. View All Shoes\n"
          "3. Re-stock Shoe\n"
          "4. Search Shoe by Code\n"
          "5. Calculate Value per Item\n"
          "6. Identify Highest Quantity Shoe\n"
          "7. Exit\n")

    choice = input("Select an option (1-8): ")

    if choice == '1':
        capture_shoes()

    elif choice == '2':
        view_all()

    elif choice == '3':
        re_stock()

    elif choice == '4':
        search_shoe()

    elif choice == '5':
        value_per_item()

    elif choice == '6':
        highest_qty()

    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please select a number between 1 and 8.")
