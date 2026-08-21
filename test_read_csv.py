from functions.read_csv import read_csv

cases = ["/path/to/data.csv"]

for case in cases:
    print(read_csv(case))
