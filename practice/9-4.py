class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("你好欢迎光临")

restaurant = Restaurant("nihao","nihao")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class Restaurant_1(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(self, restaurant_name, cuisine_type)

    def set_number_served(self, old_number):
        print(old_number)

    def increase_number_served(self, increase_number, old_number):
        print(increase_number)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "甜品")
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)

iceCreamStand = IceCreamStand("so", ["1", "2"])
iceCreamStand.show_flavors()
