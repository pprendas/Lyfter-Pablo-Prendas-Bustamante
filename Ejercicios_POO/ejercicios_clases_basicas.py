#Pasos para calcular el áreaMultiplica el radio por sí mismo (eleva el radio al cuadrado: \(r \times r\)).Multiplica ese resultado por el valor de pi (\(\pi \approx 3.1416\)).Escribe la respuesta usando unidades cuadradas (como \(\text{cm}^{2}\) o \(\text{m}^{2}\)).

class Circle:
    radius = 0
    
    def get_area(self):
        area = 3.1416 * (self.radius ** 2)
        print(f"The area of the circle with radius {self.radius} is: {area}")

Circle1 = Circle()
Circle1.radius = 5
Circle1.get_area()

#Segundo ejercicio: BUS

class person:
    name = ""
    age = 0

class Bus:
    max_passengers = 0

    def add_passengers(self,number,person):
        if self.max_passengers + number <= 50:
            self.max_passengers += number
            print(f"Added {number} passengers. Total passengers: {self.max_passengers}")
        else:
            print("Cannot add passengers. Maximum capacity reached.")
    
    def remove_passengers(self,number,person):
        if self.max_passengers - number >= 0:
            self.max_passengers -= number
            print(f"Removed {number} passengers. Total passengers: {self.max_passengers}")
        else:
            print("Cannot remove passengers. Not enough passengers on the bus.")
bus1 = Bus()
bus1.add_passengers(30, person())
bus1.add_passengers(25, person())
bus1.remove_passengers(10, person())

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

