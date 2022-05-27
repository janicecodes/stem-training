my_list=[2,4,1,7,8,10,12]
for elem in my_list:
    print(elem)

other_list=[ ]
my_list=[2,4,1,7,8,10,12]
for elem in my_list:
    print(elem)
    other_list.append(elem)
print(other_list)

my_list=[2,4,1,7,8,10,12]
other_list=[elem for elem in my_list]
print(other_list)    

for elem in my_list:
    if elem%2==0:
        other_list.append(elem)
print(other_list)

my_list=[2,4,1,7,8,10,12]
other_list=[elem for elem in my_list if elem% 2==0]
print(other_list)