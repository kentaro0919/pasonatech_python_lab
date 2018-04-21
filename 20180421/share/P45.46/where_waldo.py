import re

wally=r'Wally'
name_lst=['Wenda','Wizard Whitebeard','Wally','Woof','Odlaw','The Wally Watchers']

in_a_park=','.join(name_lst)
print(in_a_park)

waldo=r'Waldo'
walk_in_a_park=re.sub(wally, waldo, in_a_park)
print(walk_in_a_park)

waldo_candidate=re.finditer(waldo, walk_in_a_park)
for discovery in waldo_candidate:
	print('Waldo is there,It is in a range of', discovery.span())
