#convert.py
#An algorithm to convert Celsius temps to Farenheit

def main():
 print("This program lists the equivalents from Celsius and Fahrenheit")
 print("In steps of ten from 0 degrees Celsius to 100")
 for i in range(11):
  TempC = i * 10
  fahrenheit = 9 / 5 * TempC + 32

  print(TempC, "degrees Celsius =", fahrenheit, "Degrees ")

main()