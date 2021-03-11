age = 32;
name = "LeRoy"
print(age)
print(name)

print(f'Hello my name is {name} and I am {age}  years old')


if age > 19:
    print("You are old enough to ride.")
else:
    print("Not quite ready to ride.")


def hello(theString):
    print("Helllo Worlllld " + theString )

hello('Jolene')

def otherHello(name, age):
    print("Hello {} you are {} years old".format(name, age))

otherHello('Jacob', 290)

#List
catnames = ['Neo', 'Markus', 'Sheeba', 'Taylor']

catnames.insert(0, 'Janus')

print (catnames)

#Loops

for cat in catnames:
    print(cat)

#For Loop with constraints (for example 'in range')
#While Loop

#Dictionary
dogs = {'Doggo':8, 'Cattos':10, 'Jackson':1}
print(dogs)
print(dogs['Doggo'])
del(dogs['Jackson'])
dogs['Sarah'] = 123
print(dogs)

#Classes

class Dog:
    
    def __init__(self, name='', age=0, furcolor=''):
        self.name = name
        self.age = age
        self.furcolor = furcolor
    
    def bark(self):
        print('Bark!!')

# mydog = Dog()
# mydog.name = "Tropper"
# mydog.age = 18

# mydog.bark()
# print(mydog.name)
# print(mydog.age)

#Class based init 
mydog = Dog('James', 19, 'Brown')
print(mydog)