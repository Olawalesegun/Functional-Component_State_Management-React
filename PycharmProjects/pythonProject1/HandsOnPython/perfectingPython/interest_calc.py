def interest_calc(amount, no_of_year):
    # take in amount and number of years
    tax_percent = 5/100
    for count in range(1, no_of_year + 1):
        tax_calc = amount * (1+tax_percent) ** count 
        print(f"Year {count} returns an interest of : {tax_calc:,.2f}")

print(interest_calc(50, 4))


def investment(principal_amount, years):
    rate = 0.05
    for year in range(1, years + 1):
        roi = principal_amount * rate
        future_value = principal_amount + roi
        principal_amount = future_value
        print(f"year {year} return on investment is {roi}. Your principal is now {future_value}")


principal_amount = int(input("Enter the amount you want to invest: "))
years = int(input("Enter the number of years: "))
investment(principal_amount, years)

