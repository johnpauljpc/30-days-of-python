class Animal():
    sound = "Meew"
    def make_sound(self):
        return self.sound
    
    # Changing the state of the class
    def make_new_sound(self, new_sound):
        self.sound = new_sound
        return self.sound
        


obj = Animal()  # Class Instantiation
print(obj.make_sound())