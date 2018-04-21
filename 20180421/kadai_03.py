import re

test_text = ["Wenda", "Wizard Thitebeard", "Wally", "Woof", "Odlwa", "The Wally Watchrs"]

#print(','.join(test_text))

wally = re.compile(r"Wally")
match_text = re.findall(wally, ','.join(test_text))
match_text_range = [a.span() for a in re.finditer(wally, ','.join(test_text))]

print(f"{test_text} \nWally is there, it is in a range of {match_text_range} There are {len(match_text)} Wally")
