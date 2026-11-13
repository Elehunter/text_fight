from characters import Character
from combat import combat_start


def start_game():
    print(f"\nNew game started")
    player_name = input("Enter your name: ".strip())
    player = Character(name=player_name)
    print(f"Welcome to Text_Fight, {player.name}")
    input()
    print(f"starting encounter...")
    input()
    enemy = Character(name="slime", health=10, attack_power=1, defense=0)
    print(f"You encounter a {enemy.name}.")
    input()
    combat_start(player, enemy)


def main_menu():
    while True:
        print(f"===TEXT_FIGHT===")
        print(f"1. NEW GAME")
        print(f"2. EXIT")
        choice = input()
        if choice == "1":
            start_game()
        elif choice == "2":
            break
        else:
            print(f"===TEXT_FIGHT===")
            print(f"1. NEW GAME")
            print(f"2. EXIT")

if __name__ == "__main__":
    main_menu()
