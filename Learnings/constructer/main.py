class Person:
    def __init__(self, name, occupation ):
        print("Heuy Howdy")
        self.name = name
        self.occ = occupation
    def info(self):
            print(f'{self.name} is a {self.occ}')

a = Person("Vivi" , "Champ")
a.info()