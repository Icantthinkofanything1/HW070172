#This is a Python calculator program
#It allows the user to type in a mathematical expression
#The value of that expression will then be displayed

def main():
   print("This program functions as a calculator.") 
   print("You can type in your calculations and the algorithm")
   print("will compute the result. This will be repeated a 100 times.")
   print("Quit by closing the window or typing nonsense.")
   
   for i in range(100):
    x = eval(input("Type in your calculations: "))
    y = x
    print("=", y)

main()