class Car():
    def __init__(self, model , color):
        self.model = model
 
    def drive(self):
        print(f"the {self.color} {self.model} is driving.")
 
    def stop(self):
        print(f"the {self.color} {self.model} has stopped.")
 
#create instance of the car class
car1 = Car("red","Totota")
car2 = Car("blue","Honda")