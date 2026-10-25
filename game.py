import questionary
from rich.console import Console
from rich.panel import Panel

from missions import MISSIONS

console = Console()


def play_mission(mission):
    console.print(
        Panel(
            mission["description"],
            title=mission["title"],
            border_style="cyan",
        )
    )

    answer = console.input("[bold yellow]Code d'accès : [/bold yellow]")

    if check_answer(mission, answer):
        console.print(f"[bold green]{mission['success_message']}[/bold green]")
        return True

    console.print("[bold red]Accès refusé ![/bold red]")
    return False


def show_missions():
    console.print("\n[bold cyan]Missions disponibles[/bold cyan]")

    for mission in MISSIONS:
        console.print(f"{mission['id']}. {mission['title']}")


def start_game():
    score = 0

    while True:
        choice = questionary.select(
            "TERMINAL QUEST — Menu principal",
            choices=["Jouer", "Voir les missions", "Quitter"],
        ).ask()

        if choice == "Jouer":
            for mission in MISSIONS:
                if play_mission(mission):
                    score += 1

            console.print(
                f"\n[bold cyan]Score : {score}[/bold cyan]"
            )

        elif choice == "Voir les missions":
            show_missions()

        else:
            console.print("[bold green]À bientôt, agent ![/bold green]")
            break

def check_answer(mission, answer):
    return answer.strip() == mission["answer"]