from animals import Animal


class Wolf(Animal): #Child class Wolf inherits from Parent class Animal
    sound = "huuur"

class BabyWolf(Wolf): #Inherits Wolf
    pass

print(BabyWolf().sound)

print(Wolf().sound)