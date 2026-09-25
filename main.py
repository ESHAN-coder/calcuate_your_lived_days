# Read input from the user
years = int(input("Enter years: "))
months = int(input("Enter additional months: "))

# Estimate total days (365 days per year, ~30 days per month)x
total_days = (years * 365) + (months * 30)

print(f"You have lived approximately {total_days} days.")