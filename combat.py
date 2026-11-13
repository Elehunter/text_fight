def combat_start(player: Character, enemy: Character):
    turn_number = 1

    while player.is_alive() and enemy.is_alive():
        print(f"---Turn {turn_number}---")
        player.attack(enemy)
        if not enemy.is_alive():
            print(f"{enemy.name} slain!")
            break

        enemy.attack(player)
        if not player.is_alive():
            print(f"{player.name} has been vanquished on turn {turn_number}")

        turn_number += 1
        input()
