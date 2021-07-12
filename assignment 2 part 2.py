#print all the +ve numbers in a given range

#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64

#Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]

list1= [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
k1=[]
k2=[]

for num1 in list1:
    if num1>0:
        #print(num1)
        k1.append(num1)
print("k1= ",k1)

for num1 in list2:
    if num1>0:
        #print(num1)
        k2.append(num1)
print("k2= ",k2)


