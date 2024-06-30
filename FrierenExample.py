from Spell import Spell
from Frieren import Frieren
from Aura import Aura
basicSpell = Spell("Basic Spell", 50, 10)
frieren = Frieren("frieren", 5000, 20, 150)
aura = Aura("Aura", 6000, 30, 20)

undying_army = aura.summon_undying_army()

for monster in undying_army:
    frieren.cast_spell("Basic Spell", monster)
    if frieren.mana < 80:
        print(f"{frieren.name} mana is below 80.")
        break

if aura.obedience_spell(frieren):
    print(f"{aura.name} attack to control {frieren.name}")
    frieren.ultimate()
    controlled_aura = Aura.ControledCharacter(frieren, aura.name, aura.health, aura.base_attack, aura.mana)
    print(f"{frieren.name} now controls {aura.name} due to higher mana.")
    controlled_aura.take_damage(aura.health)
else:
    print(f"{frieren} attempts to control {aura.name} due to lower mana of {aura.name}.")

print("frieren casts a Basic Spell")