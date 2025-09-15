import time
import numpy as np
from colortqdm import colortqdm as ctqdm

total = 5000

print("Basic usage:")
for _ in ctqdm(range(total)):
    time.sleep(0.001)

with ctqdm(total=total, desc="Known total") as pbar:
    for i, p in enumerate(np.random.uniform(0,1,total)):
        if p > i / total:
            pbar.update(1, color="green")
        else:
            pbar.update(1, color="red")
        time.sleep(0.001)

with ctqdm(total=None, desc="Unknown total") as pbar:
    for i, p in enumerate(np.random.uniform(0,1,total)):
        if p > i / total:
            pbar.update(1, color="green")
        else:
            pbar.update(1, color="red")
        
        time.sleep(0.001)
        
total = 500

print("Available named colors:")
with ctqdm(total=total) as pbar:
    x = np.random.randint(0,10,total)
    for i in x:
        if i == 0:
            pbar.update(1, color="blue",    name="blue")
        elif i == 1:
            pbar.update(1, color="orange",  name="orange")
        elif i == 2:
            pbar.update(1, color="green",   name="green")
        elif i == 3:
            pbar.update(1, color="red",     name="red")
        elif i == 4:
            pbar.update(1, color="purple",  name="purple")
        elif i == 5:
            pbar.update(1, color="brown",   name="brown")
        elif i == 6:
            pbar.update(1, color="magenta", name="magenta")
        elif i == 7:
            pbar.update(1, color="grey",    name="grey")
        elif i == 8:
            pbar.update(1, color="yellow",  name="yellow")
        else:
            pbar.update(1)  #default (white)
        time.sleep(0.02)

with ctqdm(total=total, desc="Custom RGB") as pbar:
    x = np.random.randint(0,4,total)
    for i in x:
        # alternate between a named color and an arbitrary RGB tuple
        if i == 0:
            pbar.update(1, color=(208,244,244))
        elif i == 1:
            pbar.update(1, color=(238,213,255))
        elif i == 2:
            pbar.update(1, color=(255,192,215))
        else:
            pbar.update(1, color=(255,249,193))
        time.sleep(0.01)