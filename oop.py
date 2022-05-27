from webbrowser import get


class dog:
    def __init__(self ,no_of_eyes, color,legs):
        self.no_of_eyes = no_of_eyes
        self.color = color
        self.legs = legs
    def barking(self):
        print("woof woof") 
    def walking(self):
        print("limping") 
        pass
german_shephered =dog(no_of_eyes= 2, color='green',legs=2)
dodger =dog(no_of_eyes=2 ,color='brown',legs=2)
dobberman=dog(no_of_eyes=2 ,color='grey',legs=2)

print(german_shephered.color)
print(dodger.color)
print(dobberman.color)

dobberman.color = 'dark brown'
print(dobberman.color)
print(dobberman.legs)
dobberman.barking()
dodger.walking()