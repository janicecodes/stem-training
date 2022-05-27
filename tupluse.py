fruits=["apples","oranges","banana"]
fruits.append("cherry")
print(fruits)


fruits=["apples","oranges","banana"]
fruits.append("cherry")
fruits.remove("cherry")
print(fruits)
my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)


fruits=["apple","oranges","banana"]
fruits_2=["cherry","tomato"]
fruits_3=fruits+fruits_2
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)


fruits_4=("apple","oranges","banana")
print(fruits_4)
print(fruits_4[1])


new_list=list(fruits_4)
new_list.append("tomato")
fruits_4=tuple(new_list)


fruits_=("apples","ornges","oranges","oranges")
fruits_5={"apples","oranges","oranges","oranges"}
print(fruits_5)
