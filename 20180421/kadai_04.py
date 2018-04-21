import os
import glob

with open("test.txt", encoding="utf8") as f:
    row = f.readlines()
    
#[print(r) for r in row]
#print(help(glob))
print(glob.escape("C:\\"))

