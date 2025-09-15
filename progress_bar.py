# imports first
from rich.progress import Progress
import time

# It can be imported speedtest_here.py

# Setting-up progress bar

with Progress() as progress:

    task = progress.add_task("[speedtest_here.main()]{task.description}", total=100)

    # LOOP to update progress

    while not progress.finished:
        progress.update(task, advance=10)
        time.sleep(0.2)
