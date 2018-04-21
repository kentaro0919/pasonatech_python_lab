cinema="star wars:the empire strikes back"

titles=cinema.split(':')
#print(titles)

starwars=[]
for char in titles:
	starwars.append(char.strip())

#print(starwars)


if starwars[0].isupper():
	title=starwars[0]
else:
	title=starwars[0].upper()


if starwars[1].istitle():
	subtitle=starwars[1]
else:
	subtitle=starwars[1].title()


#print(title)
#print(subtitle)


print('\n',title.center(60))
print(subtitle.center(60))