#File: chaos.py
#A simple program illustrating chaotic behaviour.

def main():
 print("This program illustrates a chaotic function")
 x = eval(input("Enter a number between 0 and 1: "))
 n = eval(input("How many numbers should I print? "))
 for i in range(n):
  x = 2.0 * x * (1 - x)
  print (x)

main()

