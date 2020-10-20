#File: chaos.py
#A simple program illustrating chaotic behaviour.

def main():
 print("This program illustrates a chaotic function")
 x = eval(input("Enter a number between 0 and 1: "))
 for i in range(10):
  x = 2.0 * x * (1 - x)
  print (x)

main()

#Differences compared to the original chaos function: 
#The numbers become less irregular compared to the original chaos function
#They don't change anymore after the fifth loop
#This is especially the case for numbers under 1 like .25, .26, .3