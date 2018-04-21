import re

wally=r'Wally'
name_lst=['Wenda','Wizard Whitebeard','Wally','Woof','Odlaw','The Wally Watchers']

in_a_park=','.join(name_lst)
print(in_a_park)


wally_pos=re.search(wally,in_a_park)
print('Wally is there, It is in a range of',wally_pos.span())


wally_lst=re.findall(wally,in_a_park)
print('There are',len(wally_lst),'Wally.')
