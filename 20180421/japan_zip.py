import csv

with open("sample/asahikawa_zip.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    aa = [row[6:9] for row in reader if row[2] == "788205"]
print(" ".join(aa[0]))


with open("sample/hokkaido.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    aa = [row for row in reader ]#if row[2] == "788205"]
[print(a) for a in aa]


