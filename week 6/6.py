class Device:
    def turn_on(self):
        pass
 
class Fan(Device):
    def turn_on(self):
        return"fan is now spinning"
 
class Light(Device):
    def turn_on(self):
        return"Light is now on"
 
class Tv(Device):
    def turn_on(self):
        return"Tv is now on"
 
#function that uses polymorphism
def activate_device(device):
    print(device.turn_on())
 
tv = Tv()
fan = Fan()
light = Light()
 
activate_device(tv)
activate_device(fan)
activate_device(light)