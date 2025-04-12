class Car:
    def __init__(self, modal,year):
        self.modal =modal
        self.year = year
        
    def display_info(self):
        print(f"The car is '{self.year}' {self.modal}")
info = Car("Toyota", 2020)
info.display_info()
info1 = Car("Hayabusa" ,2019)
info1.display_info()