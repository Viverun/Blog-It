class Person:
    name = "JellO"
    occupation = "Floating"
    networth = 49
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = "ViVi"
# a.occupation = "Codine"
# print(a.name, a.occupation)
a.info()
