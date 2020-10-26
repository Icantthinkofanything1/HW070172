#FutureValue.py
# A program to compute the value of an investment
# carried into the future a x amount of years

def main():
 print("This program calculates the future value")
 print("of an assignable yearly investment")
 print("after an assignable span of years.")

 annual = eval(input("Type in your fixed annual investment: "))
 apr = eval(input("Enter the annual interest rate: "))
 years = eval(input("Type in the span of years: "))
 principal = annual
 
 for i in range(years):
     principal = principal * (1 + apr) + annual
 
 print("The value in", years, "years is:", principal)

main()