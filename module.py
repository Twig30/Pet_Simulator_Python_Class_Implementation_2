# This is an an incomplete 
class Pet:
    def __init__(self,name):
        self.name = name
        self.hunger = 40
        self.happiness = 50
        self.energy = 50
        # Add initialize code here
        pass # Remove 'pass' after you add additional code
    def status(self):
        return f"-----------------\n{self.name} | Hunger: {self.hunger} | Happinesss: {self.happiness} | Energy: {self.energy}\n------------------------------"
   
    def feed(self, amount):
        amount = int(amount)
        self.hunger -= amount
        return f"{self.name} eats and reduces hunger by {amount}."
    
    def play(self,amount):
        amount = int(amount)
        self.happiness += amount
        self.energy -= amount
        return f"{self.name} plays and gains {amount} happiness but loses {amount} energy ."
   
    def sleep(self, amount):
        amount = int(amount)
        self.energy += amount
        return f"{self.name} sleeps and gains {amount} energy."


    