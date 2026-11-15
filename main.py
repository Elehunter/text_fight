import sys
from characters import Player
from enemies import spawn_enemy
from combat import combat_start
from save_system import save_game, load_game


def game_loop(player):
    while player.is_alive():
        enemy = spawn_enemy("slime")
        combat_start(player, enemy)
        if not player.is_alive():
            break
        print("\n1. Next Fight")
        print("2. Save & Quit")
        choice = input()
        if choice == "2":
            save_game(player)
            sys.exit()


def start_game():
    print(f"\nNew game started")
    player_name = input("Enter your name: ").strip() or "noname"
    player = Player(name=player_name)
    print(f"Welcome to Text_Fight, {player.name}")
    input()
    game_loop(player)


def main_menu():
    while True:
        print("===TEXT_FIGHT===")
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. EXIT")
        choice = input()
        if choice == "1":
            start_game()
        elif choice == "2":
            player = load_game()
            if player:
                game_loop(player)
        elif choice == "3":
            break

if __name__ == "__main__":
    main_menu()
