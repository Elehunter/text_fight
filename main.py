player_health = 100
enemy_health = 100
turn_number = 1

while player_health > 0 or enemy_health > 0:
    print(f"You are on turn number: {turn_number}")
    turn_number += 1
    enemy_health -= 10
    print(f"enemy health now at: {enemy_health}/100")
    if enemy_health <= 0:
        print(f"Enemy defeated on turn number: {turn_number}")
        break
    player_health -= 15
    print(f"player health now at: {player_health}/100")
    if player_health <= 0:
        print(f"You have died on turn number: {turn_number}")
        break
    input()
