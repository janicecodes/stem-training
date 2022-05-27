mydict={
    "book":"Dynamics",
    "Publisher":"longhorn",
    "year":2001,
    "Authors":['Elon musk','Paul levesque'],
    "Good": True

}
# print(mydict.keys())
# print(mydict.values())
# print(mydict.get('book'))
# print(mydict.items())

def outputNme(a):
    print("hi",a)
def replacein(phrase):
    word =""
    for letter in phrase:
        if letter.lower() in "aeiou":
            word = word+"g"
        else:
            word=word+letter
    return word
   
print(replacein(input("Enter phrase: ")))
