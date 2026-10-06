#Pasos para calcular el áreaMultiplica el radio por sí mismo (eleva el radio al cuadrado: \(r \times r\)).Multiplica ese resultado por el valor de pi (\(\pi \approx 3.1416\)).Escribe la respuesta usando unidades cuadradas (como \(\text{cm}^{2}\) o \(\text{m}^{2}\)).

class Circle:
    def __init__(self, radius):
        self.radius = radius
 
    def get_area(self):
        area = 3.1416 * (self.radius ** 2)
        return area
 
 
circle1 = Circle(5)
print(f"The area of the circle with radius {circle1.radius} is: {circle1.get_area()}")
 
#Segundo ejercicio: BUS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers   
        self.passengers = []                   
 
    def add_passengers(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"Added {person.name}. Total passengers: {len(self.passengers)}")
        else:
            print("Cannot add passenger. Maximum capacity reached.")
 
    def remove_passengers(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"Removed {person.name}. Total passengers: {len(self.passengers)}")
        else:
            print("Cannot remove passenger. That person is not on the bus.")
 
 

passenger1 = Person("Ana", 20)
passenger2 = Person("Luis", 25)
 
bus1 = Bus(50)
bus1.add_passengers(passenger1)
bus1.add_passengers(passenger2)
bus1.remove_passengers(passenger1)
 
#Tercer ejercicio: Se encuentra en documento aparte debido a que es muy largo y no cabe en este archivo.

#Cuarto ejercicio: 
class head:
    def __init__(self):
        pass
        

 

class arm:
    def __init__(self, hand):
        self.hand = hand
        pass
    

class hand:
    def __init__(self):
        pass
   

class leg:
    def __init__(self, feet):
        self.feet = feet
        pass
   

class feet:
    def __init__(self):
        pass
    

class Torso:
    def __init__(self, head, right_leg, left_leg,right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        print("Torso created with head, arms, and legs.")

class Human:
    def __init__(self, torso):
        self.torso = torso

right_arm = arm(hand())
left_arm = arm(hand())
right_leg = leg(feet())
left_leg = leg(feet())

my_head = head()
my_torso = Torso(
    head=my_head,
    right_arm=right_arm,
    left_arm=left_arm,
    right_leg=right_leg,
    left_leg=left_leg,
)
my_human = Human(my_torso)

print("Human class:", type(my_human).__name__)
print("Right arm hand class:", type(my_human.torso.right_arm.hand).__name__)

