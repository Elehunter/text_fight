from characters import Player, Enemy
from combat import combat_start


def start_game():
    print(f"\nNew game started")
    player_name = input("Enter your name: ").strip() or "noname"
    player = Player(name=player_name)
    print(f"Welcome to Text_Fight, {player.name}")
    input()
    while player.is_alive():
        slime = Enemy(name="Slime")
        combat_start(player, slime)
        input()


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

if __name__ == "__main__":
    main_menu()
