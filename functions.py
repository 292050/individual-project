import pandas as pd

def verify_user(ic_number, password):
    if len(ic_number) == 12 and password == ic_number[-4:]:
        return True
    return False

def calculate_tax(income, tax_relief):
    # Placeholder calculation for demonstration. Update based on actual tax brackets.
    taxable_income = income - tax_relief
    if taxable_income <= 0:
        return 0
    elif taxable_income <= 5000:
        return taxable_income * 0.01
    elif taxable_income <= 20000:
        return 5000 * 0.01 + (taxable_income - 5000) * 0.03
    elif taxable_income <= 35000:
        return 5000 * 0.01 + 15000 * 0.03 + (taxable_income - 20000) * 0.08
    elif taxable_income <= 50000:
        return 5000 * 0.01 + 15000 * 0.03 + 15000 * 0.08 + (taxable_income - 35000) * 0.14
    else:
        return 5000 * 0.01 + 15000 * 0.03 + 15000 * 0.08 + 15000 * 0.14 + (taxable_income - 50000) * 0.21

def save_to_csv(data, filename):
    df = pd.DataFrame([data])
    try:
        existing_df = pd.read_csv(filename)
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_csv(filename, index=False)
    except FileNotFoundError:
        df.to_csv(filename, index=False)

def read_from_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None
