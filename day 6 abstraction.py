from abc import ABC, abstractmethod     
class area(ABC):    #abstraction based class
    @abstractmethod    #anotation will start with @
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_circle(self):
        pass
class square(area):
    def calculate_area(self):
        print("in square method")
    def calculate_circle(self):
        pass
class rectangle(area):
    pass
obj=square()
obj.calculate_area()
