class Cat:
    def Sound(self):
        print("Mueee...")
        
class Dog:
    def Sound(self):
        print("Vag Vag....")
        
class Sheep:
    def Sound(self):
        print("Beeee....")
        
for animal in [Cat(), Dog(), Sheep()]:
    animal.Sound()