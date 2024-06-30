from Character import Character

class Aura(Character):
    def __init__(self, name, health, base_attack, mana):
        super().__init__(name, health, base_attack, mana)
    
    def obedience_spell(self, target):
        if self.mana > target.mana:
            print(f"{self.name} has higher mana and can control {target.name}.")
        else:
            print(f"{self.name} has lower mana and is controled by {target.name}.")
        return self.mana > target.mana
    
    def summon_undying_army(self):
        print(f"{self.name} summons the Undying Army!!!")
        army = [] #軍隊
        for _ in range(1000):
            army.append(Character(f"Monster_{_+1}", 10, 1, 0))
        return army
    
    class ControledCharacter(Character):
        def __init__(self, controller, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.controller = controller
        
        def attack(self, target):
            print(f"{self.name} is controlled by {self.controller.name} and attacks {target.name}")
            super().attack(target)