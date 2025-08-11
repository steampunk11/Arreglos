from tqdm import tqdm
from rich.progress import Progress
import numpy as np
import time

np.array([1,2,3,4])

for i in tqdm(range(100)):
    time.sleep(0.05)

with Progress() as p:
    t = p.add_task("Processing...", total=100)
    while not p.finished:
        p.update(t, advance=1)
        time.sleep(0.05)    