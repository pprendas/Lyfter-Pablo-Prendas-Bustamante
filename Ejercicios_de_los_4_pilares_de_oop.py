from abc import ABC, abstractmethod
import math
#primer ejercicio de los 4 pilares de OOP
class BankAccount:
    def __init__(self , balance):
     self.balance = balance


    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes, no se puede realizar el retiro.")
        else:
            self.balance -= amount
            print(f"Retiro {amount}. Nevo saldo es: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositado {amount}. New balance is {self.balance}")





class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("No se puede retirar, el saldo mínimo no se puede violar.")
        else:
            super().withdraw(amount)
    

#Segundo ejercicio de los 4 pilares de OOP


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circule(Shape):
    def __init__(self, radio):
        self.radio = radio
        
    def calculate_area(self):
        return math.pi * self.radio ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radio
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def calculate_area (self):
        return self.lenght * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.lenght + self.width)
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

c = Circule(5)
print(c.calculate_area())       # 78.53981633974483
print(c.calculate_perimeter())  #
#Tercer ejercicio de los 4 pilares de OOP Fabrica de autos que comparte ensamblaje de autos y cada auto tiene su propio motor y chasis


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"El motor arrancó, usa {self.fuel_type} como combustible")


class Chassis:
    def __init__(self, material):
        self.material = material

    def build_frame(self):
        print(f"El chasis está hecho de {self.material}")


class Car(Engine, Chassis):
    def __init__(self, fuel_type, material):
        Engine.__init__(self, fuel_type)
        Chassis.__init__(self, material)