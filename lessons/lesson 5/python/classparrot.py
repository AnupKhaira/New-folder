class Parrot:
    species = "bird"
    def_init_(self,name,age):
    self.name=name
    self.age=age
blu= Parrot("Blu",10)
woo= Parrot("woo",15)
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} yeras old".format(woo.name, woo.age))
