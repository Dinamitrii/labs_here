# imports first
from rich.progress import Progress
import time

# Setting-up progress bar

with Progress() as progress:

    task = progress.add_task("[progress.description]{task.description}", total=100)

    # LOOP to update progress

    while not progress.finished:
        progress.update(task, advance=10)
        time.sleep(0.2)
