#Level 1 – Basics of groupby
from itertools import groupby


text= "hello   world   python"

for key,group in groupby(text):
    if key == "":
        print("space",len(list(group)))