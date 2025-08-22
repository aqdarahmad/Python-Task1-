#Create a list of your 5 favourite fruits and print it.Print the first and last elements of the list.Change the second item in the list to "Mango".Insert: Add "Watermelon" at index 2.Check existence: Write a program that asks the user for a fruit name and checks if it’s in the list.Sort the list alphabetically


fruits = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits[1]= "Mango"
fruits.insert(2,"Watermelon") 
print(fruits)

userfruit = input("Type for the name to check existence")

if userfruit in fruits:
    print(f"{userfruit} is in the list ")
else:
   print(f"{userfruit} is not in the list ") 


fruits.sort()
print(fruits)   
