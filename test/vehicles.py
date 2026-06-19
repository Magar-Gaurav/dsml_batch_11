from abc import ABC, abstractmethod
# Here vehicle is an abstract class which will be implemented by Bike and Car child classes 
class Vehicle(ABC):
    '''
       This class is an Abstract class which takes distance and rate as input from the object.

       It has 2 abstract methods named get_vehicle_name and set_vehicle_name (getter and setter)

       It has a fare calculation logic which returns the fare price
       '''
    def __init__(self,d_name,distance):
        self.d_name = d_name
        self.distance = distance
    
    @abstractmethod
    def get_vehicle_name(self):
        pass
    @abstractmethod
    def set_vehicle_name(self):
        pass
        
    # fare calculation logic
    def fare_calculation(self):
        return self.distance  * self.rate
    
class Bike(Vehicle):
    '''
        This is a child class which implements or extends the parent Vehicle class.
        Here on this class i have used rate (class attribute) which is fixed.
    '''
    rate = 40
    def __init__(self,d_name,v_name,distance):
        super().__init__(d_name,distance)
        self.v_name = v_name
    # calling getter and setter of parent class
    def get_vehicle_name(self):
        return self.v_name
    def set_vehicle_name(self,name):
        self.v_name = name
    def calculate_fare(self):
        return self.fare_calculation()
    # print details
    def print_details(self):
        print(f"\nDriver name: {self.d_name}\nVehicle: {self.get_vehicle_name()}\nDistance: {self.distance}\nFare : {self.fare_calculation()}\n\n")
class Car(Vehicle):
    '''
        This is a child class which implements or extends the parent Vehicle class.
        Here on this class i have used rate (class attribute) which is fixed
    '''
    rate = 20
    
    def __init__(self,d_name,v_name,distance):
        super().__init__(d_name,distance)
        self.v_name = v_name
    
    # calling getter and setter of parent class
    def get_vehicle_name(self):
        return self.v_name
    def set_vehicle_name(self,name):
        self.v_name = name
    # print details
    def print_details(self):
        print(f"\nDriver name: {self.d_name}\nVehicle: {self.get_vehicle_name()}\nDistance: {self.distance}\nFare : {self.fare_calculation()}\n\n")
        return self.d_name,self.get_vehicle_name(),self,self.distance,self.fare_calculation()
    def calculate_fare(self):
        return self.fare_calculation()