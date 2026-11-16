from ui import console, show_combat_status


def combat_start(player, enemy):
    turn_number = 1

    while player.is_alive() and enemy.is_alive():
        console.clear()
        console.rule(f"[bold yellow]Turn {turn_number}[/bold yellow]")
        show_combat_status(player, enemy)

        player.attack(enemy)
        if not enemy.is_alive():
            console.clear()
            console.print(f"[bold green]{enemy.name} slain![/bold green]")
            player.gain_exp(enemy.exp_reward)
            break

        enemy.attack(player)
        if not player.is_alive():
            console.clear()
            console.print(f"[bold red]{player.name} has died![/bold red]")
            break

        turn_number += 1
        input()
