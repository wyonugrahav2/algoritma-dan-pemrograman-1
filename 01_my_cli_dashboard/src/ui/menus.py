import os
from rich.console import Console
from rich.prompt import Prompt
from src.ui.components import show_header, show_table
from src.utils.file_handler import load_data
from src.logic.analytics import calculate_balance

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        show_header()
        data = load_data()
        balance = calculate_balance(data)
        
        status_color = "green" if balance >= 0 else "red"
        console.print(f"\n[bold]💰 Saldo Saat Ini:[/bold] [bold {status_color}]Rp {balance:,}[/bold {status_color}]\n")
        
        console.print("1. 📊 Lihat Semua Transaksi")
        console.print("2. ❌ Keluar")
        
        pilihan = Prompt.ask("\nPilih menu", choices=["1", "2"])
        
        if pilihan == "1":
            clear_screen()
            show_header()
            console.print("\n")
            show_table(data)
            Prompt.ask("\n[dim]Tekan Enter untuk kembali...[/dim]")
        elif pilihan == "2":
            console.print("\n[bold yellow]Sampai jumpa![/bold yellow] 👋\n")
            break