#FutureValue.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
 print("This program calculates the future value")
 print("of an investment with compounded interest.")
 print("after a time span of 10 years")

 principal = eval(input("Enter the initial principal: "))
 rate = eval(input("Enter the yearly interest rate: "))
 periods = eval(input("Number of times interest is compunded per year: "))

 for i in range(periods * 10):
     principal = principal * (1 + rate/periods)

 print("The value in 10 years is:", principal)

main()