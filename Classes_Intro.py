class Animal(object):
    # For initializing our member variables
    is_alive = True
    health = "good"

    # Constructor
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        print (self.name)
        print (self.age)


zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

hippo = Animal("Hippo", 2, False)
hippo.description()

sloth = Animal("Sloth", 3, False)
sloth.description()
ocelot = Animal("Ocelot", 4, False)
ocelot.description()

print(sloth.health)
print(hippo.health)
print(ocelot.health)
