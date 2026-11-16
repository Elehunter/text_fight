from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

console = Console()


def show_main_menu():
    console.print(
        Panel.fit(
            "[bold cyan]1.[/bold cyan] NEW GAME\n"
            "[bold cyan]2.[/bold cyan] LOAD GAME\n"
            "[bold cyan]3.[/bold cyan] QUIT",
            title="[bold yellow]=== TEXT_FIGHT ===[/bold yellow]",
            border_style="bright_blue",
        )
    )

def make_bar(current, maximum, length=20, color="green"):
    clamped = max(0, min(current, maximum))
    filled = int((clamped / maximum) * length) if maximum > 0 else 0
    empty = length - filled
    return f"[{color}]{'█' * filled}[/{color}][dim]{'░' * empty}[/dim] {current}/{maximum}"

def show_combat_status(player, enemy):
    player_card = Panel(
        f"HP  {make_bar(player.health, player.max_health, color='green')}\n"
        f"EXP {make_bar(player.exp, player.exp_to_level, color='cyan')}\n"
        f"ATK: [bold]{player.attack_power}[/bold]  DEF: [bold]{player.defense}[/bold]\n",
        title=f"[bold yellow]{player.name} (Lv. {player.level})[/bold yellow]",
        border_style="green",
    )

    enemy_card = Panel(
        f"HP  {make_bar(enemy.health, enemy.max_health, color='red')}\n"
        f"ATK: [bold]{enemy.attack_power}[/bold]  DEF: [bold]{enemy.defense}[/bold]\n ",
        title=f"[bold red]{enemy.name}[/bold red]",
        border_style="red",
    )

    console.print(Columns([player_card, enemy_card]))
