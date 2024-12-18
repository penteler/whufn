#found this on a medium article by @abil.samedov502
class Car:
    def __init__(self, brand):
        self.brand = brand
# creating an instance of the car class
car_instance = Car("Toyota")

#accessing the instance attribute
print(car_instance.brand) # output: Toyota