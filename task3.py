username = input("Enter your username:")
password = input("Enter your pswd:")

username = username.lower()
print(username)

username = username.replace(" ","_")
print(username)


print(len(password))

print("password length >= 8 ? " , len(password) >=8)
print("Is username \"admin\"" , username=="admin")
print("Is username \"1234\"" , username=="1234")
print("Is default account ?" ,username=="admin" and password=="1234")
print(f"Welcome {username} your password length is {len(password)}")
