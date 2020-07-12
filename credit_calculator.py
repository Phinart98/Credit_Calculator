import math

calc_option = input("""What do you want to calculate?
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:
""")

if calc_option == 'n':
    credit_principal = float(input("Enter the credit principal:\n"))
    monthly_payment = float(input("Enter monthly payment:\n"))
    interest = float(input("Enter credit interest:\n"))
    interest_rate = interest / 1200
    log_arg = monthly_payment / (monthly_payment - (interest_rate * credit_principal))  # log argument
    month_number = math.ceil(math.log(log_arg, (1 + interest_rate)))
    years = int(month_number / 12)
    months = month_number % 12
    if years == 0 and months != 0:
        print(f"You need {months} months to repay this credit!")
    elif years != 0 and months == 0:
        print(f"You need {years} years to repay this credit!")
    else:
        print(f"You need {years} years and {months} months to repay this credit!")

elif calc_option == 'a':
    credit_principal = float(input("Enter the credit principal:\n"))
    month_number = int(input("Enter count of periods:\n"))
    interest = float(input("Enter credit interest:\n"))
    interest_rate = interest / 1200
    monthly_payment = credit_principal * ((interest_rate * (1 + interest_rate) ** month_number)/((1 + interest_rate) ** month_number -1))
    monthly_payment = math.ceil(monthly_payment)
    print(f"Your annuity payment = {monthly_payment}")

elif calc_option == 'p':
    monthly_payment = float(input("Enter monthly payment:\n"))
    month_number = int(input("Enter count of periods:\n"))
    interest = float(input("Enter credit interest:\n"))
    interest_rate = interest / 1200
    credit_principal = monthly_payment / ((interest_rate * (1 + interest_rate) ** month_number)/((1 + interest_rate) ** month_number -1))
    credit_principal = round(credit_principal)
    print(f"Your credit principal = {credit_principal}")