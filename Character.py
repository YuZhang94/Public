from Weapon import Weapon 
from Spell import Spell
from Skill import Skill

class Character:
    def __init__(self, name, health, base_attack, maxhealth=100, mana=150, leve=0):
        self.name = name
        self.health = health
        self.base_attack = base_attack
        self.weapon = None
        self.mana = mana
        self.maxhealth=maxhealth
        self.leve=leve
        self.spells = []
        self.skills = []

    def getAbility(self):
        print(f'{self.name} 生命 {self.health} 攻擊力 {self.base_attack} 魔力 {self.mana} 等級 {self.leve}')

    def attack(self, other):
        total_attack = self.base_attack+(self.weapon.attack_bonus if self.weapon else 0)
        print(f'{self.name} attacks {other.name} with {total_attack} damage.')
        other.take_damage(total_attack)
        
    def take_damage(self, damage):
        self.health = self.health - damage
        print(f'{self.name} took {damage} damage. Remaining health {self.health}.' )
        if self.health <= 0:
            print(f'{self.name} deads')
            
    def cast_spell(self, spell_name, target):
        for spell in self.spells:
            if spell.name == spell_name:
                spell.cast(self, target)
                break
            
    def use_skill(self,skill_name, target):
        for skill in self.skills:
            if skill_name == 'Heal':
                effect=skill.getEffect()
                print(f'{self.name} uses {skill.name}')
                effect.effect(target)
                break


    def chang_weapon(self, weapon):
        self.weapon = weapon
        print(f'{self.name} equipped {weapon}')
        
    def learn_spell(self, spell):
        self.spells.append(spell)

    def learn_skill(self, skill):
        self.skills.append(skill)
        
class heal_effect:
    def __init__(self):
        pass
    
    def effect(self, character):
        heal_amount = 20
        if character.health<character.maxhealth-20:
            character.health = character.health + heal_amount
        elif character.health>character.maxhealth-20 and character.health<=character.maxhealth:
            character.health = character.maxhealth
        else:
            print(f'{character.name} is max health')
        print(f'{character.name} is healed for {heal_amount} health points.character health {character.health}')


# sword = Weapon('Sword', 5)
# bow = Weapon('Bow', 3)


# fireBall = Spell('Fire ball',10 ,25)
# iceBall = Spell('Ice ball',5 ,15)
# thunderBall = Spell('Thunder ball',20 ,40)

# heal = Skill('Heal', heal_effect())

# hero = Character('Hero', 100, 10)
# moster = Character('Moster', 10, 1)
# moster2 = Character('Moster2', 10, 1)
# moster3 = Character('Moster3', 10, 1)
# boss = Character('Boss', 99999, 100)

# hero.chang_weapon(sword)

# hero.learn_spell(fireBall)
# hero.learn_spell(iceBall)
# hero.learn_spell(thunderBall)

# hero.learn_skill(heal)

# hero.cast_spell('Fire ball', moster)
# hero.attack(moster2)
# hero.use_skill('Heal', hero)
# boss.attack(hero)

