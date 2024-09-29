from character import Character

class Berserk(Character):
    max_health = 100

    def __init__(self, name, health, damage, defence):
        super().__init__(name, health, damage, defence)
        self.max_health = health
        self.last_chance_used = False  # Флаг для механики последнего шанса

    def __str__(self):
        return super().__str__() + \
            f" Дод. шкода: {self.count_additional_damage()}"

    def count_additional_damage(self):
        return round(max(self.damage * (1 - self.health / self.max_health), 0), 2)

    def attack(self, target):
        return target.take_damage(
            self.damage + self.count_damage_offset() + self.count_additional_damage()
        )

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            if not self.last_chance_used:
                self.health = 1
                self.last_chance_used = True
                print(f"{self.name} використав останній шанс! Здоров'я: 1")
            else:
                self.health = 0
                print(f"{self.name} був переможений!")

        return self.health