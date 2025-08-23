mytuple = ("noor" , 5 ,1,True)
#  error can't modify values tuple[0] = "nor"

#print(tuple[0:3])
#print(tuple[:2])

list1 = list(mytuple)

list1[0] = "nor"

mytuple=tuple(list1)

#print(mytuple)


