#convert.py
#An algorithm to convert Celsius temps to Farenheit

def main():
 print("This program converts temperatures from Celsius to Farenheit")
 Celsius = eval(input("What is the temperature in Celsius "))
 fahrenheit = 9/5 * Celsius + 32
 print("The temperature is", fahrenheit, "degrees Fahrenheit.")
 
 input("Press the <Enter> key to quit.")

main()