#1. Create a program that stores fruit prices in a dictionary and lets the user enter a fruit name. 
# If the fruit exists in the dictionary, print its price.
# If the fruit doesn’t exist, print "Sorry, this fruit is not available.


Fruit_Prices = {
    "Apple" : 5.5 ,
    "Banana" : 6.7 ,
    "orange" : 8.8 ,
    "mango" : 9.9 ,
}

Input_Fruit_User = input("Enter new fruit name: ")

if Input_Fruit_User in Fruit_Prices:
    print(f"The price of {Input_Fruit_User} is ${Fruit_Prices[Input_Fruit_User]}")
else:
    print("Sorry , this fruit is not available ")    