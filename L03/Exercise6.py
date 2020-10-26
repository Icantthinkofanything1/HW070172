#FutureValue.py
# A program to compute the value of an investment
# carried into the future a x amount of years

def main():
 print("This program calculates the future value")
 print("of a x yearlong investment.")

 principal = eval(input("Enter the initial principal: "))
 apr = eval(input("Enter the annual interest rate: "))
 years = eval(input("Type in the span of years: "))
 for i in range(years):
     principal = principal * (1 + apr)

 print("The value in", years, "years is:", principal)

main()