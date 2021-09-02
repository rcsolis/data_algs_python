# Write and read files
import os
from pathlib import Path

path_file = Path(__file__).resolve().parent / "./filesample.txt"

with open(os.fspath(path_file), mode="at") as f:
    f.write("\nHello from python")

with open(os.fspath(path_file), mode="rt") as f:
    print(f.read())
