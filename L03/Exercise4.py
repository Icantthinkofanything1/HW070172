#convert.py
#An algorithm to convert Celsius temps to Farenheit

def main():
 print("This program converts the temperature in Celsius into Farenheit") 
 for i in range(5):
  celsius = eval(input("Type a temperature in Celsius: "))
  fahrenheit = 9/5 * celsius + 32
    
  print("The temperature is", fahrenheit, "degrees Fahrenheit")
 
 input("Press the <Enter> key to quit.")

main()