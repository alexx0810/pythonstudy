from character import Character

player1 = Character("Vasya", 100, 10, 2)
player2 = Character("Petya", 100, 8, 3)

print(f"Створено нового персонажа: {player1.name}")
print(f"Створено нового персонажа: {player2.name}")

player1.show_stats()
player2.show_stats()

def perform_attack(attacker, defender):
    effective_damage = max(0, attacker.damage - defender.defence)
    defender.health -= effective_damage
    print(f"{attacker.name} атакує {defender.name}, наносячи {effective_damage} шкоди!")
    if defender.health <= 0:
        print(f"{defender.name} було переможено!")
    else:
        print(f"У {defender.name} залишилося {defender.health} здоров'я.")


while player1.health > 0 and player2.health > 0:
    perform_attack(player1, player2)
    if player2.health <= 0:
        break

    perform_attack(player2, player1)
    if player1.health <= 0:
        break

print(f"\nБитва закінчена!")
player1.show_stats()
player2.show_stats()


