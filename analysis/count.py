import csv
import json

from collections import Counter
from pathlib import Path

with Path("output/dataset.csv").open() as infile:
    reader = csv.DictReader(infile)
    in_care_home = [
        row["in_care_home"] for row in reader
    ]

counts = Counter(in_care_home)

with Path("output/count.json").open("w") as outfile:
    json.dump(counts, outfile)

