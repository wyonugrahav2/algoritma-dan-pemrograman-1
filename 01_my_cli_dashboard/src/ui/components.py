from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show_header():
    console.print(Panel("[bold cyan]🚀 CLI Dashboard - Financial Tracker[/bold cyan]", style="bold blue", expand=False))

def show_table(data_list):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", justify="center", style="dim")
    table.add_column("Tipe", justify="center")
    table.add_column("Jumlah (Rp)", justify="right", style="bold")
    table.add_column("Keterangan")
    
    for item in data_list:
        tipe = "[green]Masuk[/green]" if item['type'] == 'income' else "[red]Keluar[/red]"
        table.add_row(str(item['id']), tipe, f"{item['amount']:,}", item['desc'])
    
    console.print(table)