# Bank Loan Calculator - PS No. 48
# Calculates EMI, total payable amount, total interest, and loan eligibility.

def calculate_emi(principal, annual_rate, tenure_months):
    """Return monthly EMI rounded to two decimal places."""
    if annual_rate == 0:
        return round(principal / tenure_months, 2)

    monthly_rate = annual_rate / (12 * 100)
    factor = (1 + monthly_rate) ** tenure_months
    emi = principal * monthly_rate * factor / (factor - 1)
    return round(emi, 2)


def calculate_total_payable(emi, tenure_months):
    """Return the total amount payable over the loan tenure."""
    return round(emi * tenure_months, 2)


def calculate_total_interest(total_payable, principal):
    """Return the total interest paid on the loan."""
    return round(total_payable - principal, 2)


def check_eligibility(emi, monthly_income):
    """A loan is eligible when EMI is at most 40% of monthly income."""
    maximum_allowed_emi = monthly_income * 0.40
    return emi <= maximum_allowed_emi, maximum_allowed_emi


def validate_inputs(principal, annual_rate, tenure_months, monthly_income):
    """Validate all user inputs. Return an error message or None."""
    if principal <= 0:
        return "Invalid loan amount.\nEnter a positive amount."
    if not 0 <= annual_rate <= 30:
        return "Invalid annual interest rate.\nEnter a rate from 0 to 30."
    if not 1 <= tenure_months <= 360:
        return "Invalid loan tenure.\nEnter tenure from 1 to 360 months."
    if monthly_income <= 0:
        return "Invalid monthly income.\nEnter a positive income."
    return None


def main():
    print("=== Bank Loan Calculator ===")
    try:
        principal = float(input("Enter loan amount (Rs.): "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        tenure_months = int(input("Enter loan tenure (months): "))
        monthly_income = float(input("Enter monthly income (Rs.): "))
    except ValueError:
        print("Invalid input. Please enter numeric values in the correct format.")
        return

    error = validate_inputs(principal, annual_rate, tenure_months, monthly_income)
    if error:
        print(error)
        return

    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payable = calculate_total_payable(emi, tenure_months)
    total_interest = calculate_total_interest(total_payable, principal)
    eligible, maximum_allowed_emi = check_eligibility(emi, monthly_income)

    print(f"EMI: Rs.{emi:.2f}")
    print(f"Total Payable: Rs.{total_payable:.2f}")
    print(f"Total Interest: Rs.{total_interest:.2f}")
    if eligible:
        print("Eligible: Yes")
    else:
        print(f"Maximum allowed EMI (40% of income): Rs. {maximum_allowed_emi:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit.")


if __name__ == "__main__":
    main()
