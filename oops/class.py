class Mobile:
    def __init__(self, brand, battery, ram, camera, price):
        self.brand = brand
        self.battery = battery
        self.ram = ram
        self.camera = camera
        self.price = price
    def display(self):
        print("brand: ", self.brand)
        print("battery: ", self.battery)
        print("ram: ", self.ram)
        print("camera: ", self.camera)
        print("price: ", self.price)
obj = Mobile("iphone13", "4000mah", "8gb", "50mp", "70000")
obj.display()