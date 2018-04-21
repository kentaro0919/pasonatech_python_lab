from datetime import datetime

tokyo_olympics=datetime(2020,7,24,0,0,0)
today=datetime.today()

left_days=tokyo_olympics - today

signboard_top='東京オリンピック'
signboard_bottom='開催まであと' + str(left_days.days) + '日'
signboard_slogan='みんなの力で成功させよう'

deco='='
width=20

print(deco * (width + 12))
print(signboard_top.ljust(width))
print(signboard_bottom.rjust(width))
print(signboard_slogan.rjust(width))
print(deco * (width+12))

