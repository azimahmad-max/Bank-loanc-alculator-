# Bank Loan Calculator (PS No. 48)

## 1. Project overview
Bank Loan Calculator is a console-based Python 3 program. It calculates a bank loan's monthly Equated Monthly Instalment (EMI), total payable amount, and total interest. It also checks whether the EMI is affordable under the project's income rule.

## 2. Objectives
- Calculate monthly EMI using the standard reducing-balance EMI formula.
- Calculate total payable amount and total interest.
- Check eligibility using 40% of monthly income.
- Validate user input and handle zero-interest loans safely.
- Organize calculations into separate reusable functions.

## 3. Features
- Supports annual interest rates from 0% through 30%.
- Supports loan tenures from 1 through 360 months.
- Rejects non-positive loan amounts and monthly incomes.
- Handles a 0% interest rate without division by zero.
- Rounds EMI to two decimal places before calculating total payable.
- Displays all monetary results to two decimal places.

## 4. Requirements
- Python 3.8 or later (no third-party packages required).
- A terminal or command prompt.

## 5. Files
- `one.py` — complete project source code.
- `README.md` — project documentation.
- `screenshots/` — console evidence for each supplied test case.
- `BankLoanCalculator_Test_Report.pdf` — combined test report and screenshots.

## 6. How to run
1. Save `one.py` to your computer.
2. Open a terminal in the same folder.
3. Run:
   ```bash
   python one.py
   ```
4. Enter the loan amount, annual interest rate, tenure in months, and monthly income when prompted.

## 7. Input details
The program requests four values:
1. Loan amount/principal in rupees (must be greater than 0).
2. Annual interest rate (0 to 30, inclusive).
3. Loan tenure in months (1 to 360, inclusive).
4. Monthly income in rupees (must be greater than 0).

## 8. Calculation rules
Let:
- `P` = principal amount
- `r` = monthly interest rate = annual rate / 12 / 100
- `n` = tenure in months

For a non-zero interest rate:

`EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)`

For a zero interest rate:

`EMI = P / n`

The EMI is rounded to two decimal places first. Then:
- `Total Payable = rounded EMI * n`
- `Total Interest = Total Payable - P`
- `Maximum Allowed EMI = 40% * monthly income`

The applicant is eligible when `EMI <= Maximum Allowed EMI`.

## 9. Output details
For a valid loan, the program prints EMI, total payable, total interest, and the eligibility result. If the EMI exceeds 40% of monthly income, it prints the maximum allowed EMI and an ineligibility message. Invalid inputs produce a clear validation message.

## 10. Functions used
- `calculate_emi()` — calculates and rounds monthly EMI.
- `calculate_total_payable()` — calculates total repayment.
- `calculate_total_interest()` — calculates total interest.
- `check_eligibility()` — compares EMI with 40% of income.
- `validate_inputs()` — checks the input ranges.
- `main()` — collects input, calls the functions, and displays results.

## 11. Test cases
All four test cases supplied in the project sheet were run individually. Their console outputs are included in the PDF report and in the `screenshots` folder.

| Test | Principal | Rate | Tenure | Monthly income | Expected result |
|---|---:|---:|---:|---:|---|
| 1 | Rs. 500,000 | 10% | 60 months | Rs. 50,000 | EMI Rs. 10,623.52; Eligible |
| 2 | Rs. 120,000 | 0% | 12 months | Rs. 30,000 | EMI Rs. 10,000.00; Eligible |
| 3 | Rs. -50,000 | 9% | 24 months | Not requested | Invalid loan amount |
| 4 | Rs. 1,000,000 | 9% | 120 months | Rs. 20,000 | EMI Rs. 12,667.58; Not eligible |

## 12. Notes
The program follows the supplied project-sheet rules. For the invalid-input test case, validation stops at the first invalid field, so the program does not continue to calculate an EMI.
