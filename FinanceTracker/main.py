expenses = []
incomes = []

import json

def save_financial_data(expenses, incomes, filename='finance_data.json'):
    data = {'expenses': expenses, 'incomes': incomes} 
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            print("Data saved successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def load_financial_data(filename=''):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['expenses'], data['incomes']
    except FileNotFoundError:
        print(f"The file {filename} could not be found, making a new one")
        return [], []
    except json.JSONDecodeError:
        print("An error occurred while decoding the JSON data")
        return [], []
    except Exception  as e:
        print(f"An error occurred while loading the file: {e}")

def add_financial_entry(entries_list, entry_type):
    try:
        category = input(f"Enter the category for the {entry_type}: ")
        amount = float(input(f"Enter the amount for the {entry_type}: "))
        entries_list.append({"category": category, "amount": amount})
        print(f"{entry_type.capitalize()} added: {category} - ${amount} successfully")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def user_interface():
    expenses, incomes = load_financial_data()
    while True:
        choice = input("Select an option: ")
        print("\nOptions: [1] Add Expense [2] Add Income [3] Save and Exit")
        if choice == '1':
            add_financial_entry(expenses, 'expense')
        elif choice == '2':
            add_financial_entry(incomes, 'income')
        elif choice == '3':
            save_financial_data(expenses, incomes)
            break
        else:
            print("Invalid option. Please select a valid option.")
      
user_interface()

