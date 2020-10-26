#convert.py
#An algorithm to convert Fahrenheit temps into Celsius

def main():
 print("This program converts the temperature from ")
 print("Fahrenheit into Celsius")
 
 fahrenheit = eval(input("What is the temperature in Fahrenheit "))
 celsius = ((fahrenheit - 32) * 5)/9
 print("The temperature is", celsius, "degrees Celsius.")

main()