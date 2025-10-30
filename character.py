import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def attack(self, other): 
        ran_int = random.randint(30, 90)
        ran_perc = (ran_int / 100) 
        an_pwr = round(self.attack_power * ran_perc, 4)
        other.hp = round(other.hp - ran_pwr, 4)
        print(f"{self.name} attacks {other.name} for {ran_pwr} damage!")
        
    def is_alive(self):
        return self.hp > 0
    
    def __str__(self): 
        return f"{self.name}: {self.hp} HP"
    
