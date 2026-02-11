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
    
    def check_health(self):
        print(self.status())
        if self.hunger < 40:
            if self.happiness >= 50:
                if self.energy >= 50:
                    return f"{self.name} is healthy!."   
                else: return f"{self.name} isnt healthy,they are not well rested."
            else: return f"{self.name} isnt healthy, they are not happy."    
        else: return f"{self.name} isnt healthy, they arent well fed."        
            


    