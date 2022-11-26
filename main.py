class Dog:
    def __init__(self, name, healthy , birth , brother, sister, age, death ):
        self.name = name
        self.healthy = healthy
        self.birth = birth
        self.brother = brother
        self.sister = sister
        self.age = age
        self.death = death
    def info(self):
        print(f'Name: {self.name}\nHealthy: {self.healthy}\nBirth: {self.birth}\nBrother: {self.brother}\nSister: {self.sister}\nAge: {self.age}\nDeath: {self.death}')

s1 = Dog("Boben", "sick", "24/04/2022","None","None","4months","30/12/2030")
s1.info()