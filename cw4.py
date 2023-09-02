def my_name():
    print(" My name is nabila") 

my_name()


def  my_meal(food , drink):
    print(f"i like to eat {food} and while drinking {drink}")
my_meal("pizza", "cola")

def cube(number):
    return number**3

print(cube(3))


def by_three(number):
    if number%3==0 :
        return cube(number)
    else:
        return False
    
by_three(90)
    

