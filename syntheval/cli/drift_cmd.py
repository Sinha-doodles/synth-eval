"""CLI subcommand for drift detection."""
import typer
from rich.console import Console
from syntheval.evaluators.drift import population_stability_index

console = Console()

def check_drift(baseline: str, current: str):
    base_scores = [float(x.strip()) for x in baseline.split(",") if x.strip()]
    cur_scores = [float(x.strip()) for x in current.split(",") if x.strip()]
    psi = population_stability_index(base_scores, cur_scores)
    status = "[bold red]DRIFT DETECTED[/bold red]" if psi > 0.20 else "[bold green]STABLE[/bold green]"
    console.print(f"PSI: {psi:.4f} - {status}")
