class Spell:
    def __init__(self, name ,mana_cost, damage):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
    
    def cast(self, caster ,target):
        if caster.mana >= self.mana_cost:
            caster.mana = caster.mana - self.mana_cost
            print(f'{caster.name} casts {self.name}, dealing {self.damage} damage to {target.name}\n')
            target.take_damage(self.damage)
        else:
            print(f'{caster.name}沒有足夠魔力\n')