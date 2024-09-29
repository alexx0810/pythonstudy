import random
from character import Character

class Ninja(Character):
    def __init__(self, name, health, damage, defence, dodge_chance):
        super().__init__(name, health, damage, defence)
        self.dodge_chance = dodge_chance  # Ймовірність ухилення (значення від 0 до 1)

    def take_damage(self, damage):

        if random.random() <= self.dodge_chance:
            print(f"{self.name} ухилився від атаки!")
            return 0
        else:

            return super().take_damage(damage)

    def __str__(self):
        return super().__str__() + f' Ймовірність ухилення: {self.dodge_chance * 100}%\n'

ninja = Ninja(name="Ніндзя", health=100, damage=10, defence=20, dodge_chance=0.3)

ninja.show_stats()

opponent = Character(name="Суперник", health=120, damage=15, defence=10)
damage_dealt = opponent.attack(ninja)
print(f"Суперник завдав {damage_dealt} шкоди!")
