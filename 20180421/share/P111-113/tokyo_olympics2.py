import datetime

tokyo2020_str='2020-07-24 17:30:00'

tokyo2020=datetime.datetime.strptime(tokyo2020_str,'%Y-%m-%d %H:%M:%S')
print('Olympics YEAR is' ,tokyo2020.year)

