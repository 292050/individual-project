import pandas as pd
from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

def main():
    filename = 'tax_records.csv'
    registered_users = read_from_csv(filename)

    while True:
        print("Welcome to the Malaysian Tax Input Program!")
        user_id = input("Enter your ID: ")
        ic_number = input("Enter your IC number: ")

        if registered_users is not None and ic_number in registered_users['IC Number'].values:
            password = input("Enter the last 4 digits of your IC number as password: ")
            if verify_user(ic_number, password):
                print("Login successful!")
            else:
                print("Invalid credentials. Please try again.")
                continue
        else:
            print("You are not registered. Please register first.")
            password = input("Set your password (last 4 digits of your IC number): ")
            if verify_user(ic_number, password):
                print("Registration successful!")
            else:
                print("Invalid IC number or password. Registration failed.")
                continue

        annual_income = float(input("Enter your annual income: "))
        tax_relief = float(input("Enter your total tax relief amount: "))
        tax_payable = calculate_tax(annual_income, tax_relief)

        print(f"Your tax payable is: RM {tax_payable:.2f}")

        user_data = {
            'ID': user_id,
            'IC Number': ic_number,
            'Annual Income': annual_income,
            'Tax Relief': tax_relief,
            'Tax Payable': tax_payable
        }
        save_to_csv(user_data, filename)

        another = input("Do you want to enter another record? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thank you for using the Malaysian Tax Input Program!")

if __name__ == "__main__":
    main()
