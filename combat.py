def combat_start(player, enemy):
    turn_number = 1

    while player.is_alive() and enemy.is_alive():
        print(f"---Turn {turn_number}---")
        player.attack(enemy)
        if not enemy.is_alive():
            print(f"\n{enemy.name} slain!")
            player.gain_exp(enemy.exp_reward)
            break

        enemy.attack(player)
        if not player.is_alive():
            print(f"{player.name} has died!")

        turn_number += 1
        input()
