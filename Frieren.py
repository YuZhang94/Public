from Character import Character

class Frieren(Character):
    def __init__(self, name, health, base_attack, mana=100):
        super().__init__(name, health, base_attack, mana)
        self.hidden_mana = True #新增一個屬性來標記mana是否隱藏
    
    def cast_spell(self, spell_name, target):
        if self.mana>=10:
            self.mana -= 10
            print(f"{self.name} casts a {spell_name} on {target.name}")
            print(f"{self.name} mana is {self.mana}")
            target.take_damage(target.health) #秒殺
        else:
            print("f{self.name} does not have enough mana to cast the spell.")

    def displayed_mana(self):
        if self.hidden_mana:
            return 150
        else:
            return self.mana

    def ultimate(self): #大招
        self.mana = 999999
        self.hidden_mana = False
        print(f"{self.name} has unleashed their ultimate power! Mana is now {self.displayed_mana()}") # Corrected this line
