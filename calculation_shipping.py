import abc

class ShippingMethod(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_cost(self):
        pass

    @abc.abstractmethod
    def calculate_time(self):
        pass

class GroundShipping(ShippingMethod):
    def __init__(self, width, length, height, weight, distance, shipping_type):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.distance = distance
        self.shipping_type = shipping_type

    def calculate_cost(self):
        cost_per_kilometer = 0.1
        cost_per_kilogram = 1.5
        cost_per_cubic_meter = 0.5
        ratio = 2 if self.shipping_type == 'fast' else 1
        return (self.distance * cost_per_kilometer + self.weight * cost_per_kilogram + self.width * self.length * self.height * cost_per_cubic_meter) * ratio

    def calculate_time(self):
        ratio = 0.5 if self.shipping_type == 'fast' else 1
        # Швидкість руху км/год
        speed = 120
        return (self.distance / speed) * ratio

class AirShipping(ShippingMethod):
    def __init__(self, width, length, height, weight, distance, shipping_type):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.distance = distance
        self.shipping_type = shipping_type

    def calculate_cost(self):
        cost_per_kilometer = 1.0
        cost_per_kilogram = 5
        cost_per_cubic_meter = 1.0
        ratio = 2 if self.shipping_type == 'fast' else 1
        return (self.distance * cost_per_kilometer + self.weight * cost_per_kilogram + self.width * self.length * self.height * cost_per_cubic_meter) * ratio

    def calculate_time(self):
        ratio = 0.5 if self.shipping_type == 'fast' else 1
        # Швидкість руху км/год
        speed = 800
        return (self.distance / speed) * ratio

class SeaShipping(ShippingMethod):
    def __init__(self, width, length, height, weight, distance, shipping_type):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.distance = distance
        self.shipping_type = shipping_type

    def calculate_cost(self):
        cost_per_kilometer = 0.5
        cost_per_kilogram = 2
        cost_per_cubic_meter = 0.3
        ratio = 2 if self.shipping_type == 'fast' else 1
        return (self.distance * cost_per_kilometer + self.weight * cost_per_kilogram + self.width * self.length * self.height * cost_per_cubic_meter) * ratio

    def calculate_time(self):
        ratio = 0.5 if self.shipping_type == 'fast' else 1
        # Швидкість руху км/год
        speed = 450
        return (self.distance / speed) * ratio

class ShippingCalculatorFactory:
    def create_shipping_calculator(self, method, width, length, height, weight, distance, shipping_type):
        if method == 'ground':
            return GroundShipping(width, length, height, weight, distance, shipping_type)
        elif method == 'air':
            return AirShipping(width, length, height, weight, distance, shipping_type)
        elif method == 'sea':
            return SeaShipping(width, length, height, weight, distance, shipping_type)
        else:
            raise ValueError("Unsupported shipping method")

def display_menu():
    print("Menu:")
    print("1. Calculate the cost of shipping")
    print("2. Exit")

def shipping_client():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            factory = ShippingCalculatorFactory()
            method = input("Enter the shipping method (ground/air/sea): ")
            width = float(input("Enter the width of the package (meter): "))
            length = float(input("Enter the length of the package (meter): "))
            height = float(input("Enter the height of the package (meter): "))
            weight = float(input("Enter the weight of the package (kilogram): "))
            distance = float(input("Enter the shipping distance (kilometer): "))
            shipping_type = input("Type of shipping (fast/normal): ")

            shipping = factory.create_shipping_calculator(method, width, length, height, weight, distance, shipping_type)

            print(f"The cost of shipping using {method} method is: {shipping.calculate_cost()} dollars")
            print(f"The estimated time of {shipping_type} shipping is: {shipping.calculate_time()} hours")

        elif choice == '2':
            print("Thank you for using the program!")
            break
        else:
            print("Wrong choice. Please try again.")

if __name__ == "__main__":
    shipping_client()
