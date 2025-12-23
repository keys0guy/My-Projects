import math

# get either "investment" or "bond" from user
#
# if investment
# get amount of money, interest rate, number of years to invest, simple or compound interest
# return total amount after interest
#
# if bond
# get value of house, interest rate, number of months to repay bond
# return monthly repayment amount

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.\n")

choice = input('Enter either "investment" or "bond" from the menu above to proceed: ').lower()                       # choose calculator type

if choice == "investment":                                                                                          # investment calculation
    amount = float(input("Please enter the amount of money you are depositing: "))
    rate = float(input("Please enter your interest rate as a percentage (e.g., 8 for 8%): ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ").lower()       # specify interest type for embedded if statement

    if interest_type == "simple":
        total_amount = amount * (1 + rate * years)
    elif interest_type == "compound":
        total_amount = amount * math.pow((1 + rate), years)
    else:
        print("Invalid interest type selected.")
        interest_type = input("Please enter 'simple' or 'compound': ").lower()

elif choice == "bond":                                                                                              # bond calculation
    amount = float(input("Please enter your house's value: "))
    rate = float(input("Please enter your interest rate as a percentage (e.g., 8 for 8%): ")) / 100 / 12
    months = int(input("Please enter the number of months you plan to take to repay the bond: "))

    total_amount = (rate * amount) / (1 - (1 + rate) ** (-months))

else:                                                                                                               # invalid choice handling
    choice = input("Invalid choice. Please enter either 'investment' or 'bond': ").lower()

print("Your total amount is" , round(total_amount, 2),".")
