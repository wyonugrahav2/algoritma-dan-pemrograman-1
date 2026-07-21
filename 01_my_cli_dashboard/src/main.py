from src.ui.menus import main_menu
from rich.console import Console

console = Console()

def main():
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]Keluar dari aplikasi... Sampai jumpa![/bold red]")

if __name__ == '__main__':
    main()