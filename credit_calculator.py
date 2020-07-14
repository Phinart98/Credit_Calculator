import math
import argparse
import sys

if __name__ == "__main__":
    # initialize the parser
    parser = argparse.ArgumentParser(description="Welcome to the Credit Calculator!!!")

    # Add the optional parameters
    parser.add_argument("--type")
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=float)

    # parse the arguments
    args = parser.parse_args()

    if args.type is None:
        print("Incorrect parameters. Include a calclation type-annuity or differentiated.")
        exit()

    if args.type != "diff" and args.type != "annuity":
        print("Incorrect parameters. type can only be annuity or differentiated.")
        exit()


    if len(sys.argv) < 5:
        print("Incorrect parameters. Make sure your arguments are 4 in number.")
        exit()

    if args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters. Do not include the payment parameter for a differentiated payment request.")
            exit()
        elif args.interest is None:
            print("Incorrect parameters. Include the interest in your arguments.")
            exit()
        elif args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters. All numerical parameters must be non-negative.")
            exit()
        else:
            total = 0
            interest_rate = args.interest / 1200
            for month in range(args.periods):
                differentiated_monthly = math.ceil((args.principal / args.periods) + interest_rate * (args.principal - ((args.principal * ((month + 1) - 1)) / args.periods)))
                print(f"Month {month + 1}: paid out {differentiated_monthly}")
                total += differentiated_monthly
            print()
            overpayment = int(total - args.principal)
            print(f"Overpayment = {overpayment}")

    elif args.type == "annuity":
        if args.interest is None:
            print("Incorrect parameters. Include the interest rate")
            exit()
        elif args.periods is None:
            if args.principal < 0 or args.interest < 0 or args.payment < 0:
                print("Incorrect parameters. All numerical parameters must be non-negative.")
                exit()
            interest_rate = args.interest / 1200
            log_arg = args.payment / (args.payment - (interest_rate * args.principal))  # log argument
            month_number = math.ceil(math.log(log_arg, (1 + interest_rate)))
            years = int(month_number / 12)
            months = month_number % 12
            if years == 0 and months != 0:
                print(f"You need {months} months to repay this credit!")
            elif years != 0 and months == 0:
                print(f"You need {years} years to repay this credit!")
            else:
                print(f"You need {years} years and {months} months to repay this credit!")
            args.periods = month_number

        elif args.payment is None:
            if args.principal < 0 or args.periods < 0 or args.interest < 0:
                print("Incorrect parameters. All numerical parameters must be non-negative.")
                exit()
            interest_rate = args.interest / 1200
            monthly_payment = args.principal * ((interest_rate * (1 + interest_rate) ** args.periods)/((1 + interest_rate) ** args.periods -1))
            monthly_payment = math.ceil(monthly_payment)
            print(f"Your annuity payment = {monthly_payment}!")
            args.payment = monthly_payment

        elif args.principal is None:
            if args.periods < 0 or args.interest < 0 or args.payment < 0:
                print("Incorrect parameters. All numerical parameters must be non-negative.")
                exit()
            interest_rate = args.interest / 1200
            credit_principal = args.payment / ((interest_rate * (1 + interest_rate) ** args.periods)/((1 + interest_rate) ** args.periods -1))
            credit_principal = math.floor(credit_principal)
            print(f"Your credit principal = {credit_principal}!")
            args.principal = credit_principal

        overpayment = int((args.payment * args.periods) - args.principal)
        print(f"Overpayment = {overpayment}")
