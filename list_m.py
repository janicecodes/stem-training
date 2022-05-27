#for loop in python
mangoes="Book"
for i in mangoes:
    print(i)
    print("Done")

#for loops with lists
words=["I","DID","A"]
for word in words:
    print(word + "I")
#counting letters in string
str= "Hello guys welcome back to my class"
count=0
for x in str:
    if (x=='o'):
        count +=1
print("the number of o's :",count)
str= "Hello guys welcome back to my class"
for x in str:
    if (x=='l'):
        continue
    else:
        print(x)
