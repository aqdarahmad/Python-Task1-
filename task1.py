name = input("enter your name: ")

notes = input("enter some notes ")

filename = "usernotes.txt"

with open("usernotes.txt","a" ) as file:
    
     file.write(f"name: {name}, notes: {notes}\n")

print("Successfully save data!")  

with open(filename , "r" ) as file:
    content = file.read()
    print(content)
    