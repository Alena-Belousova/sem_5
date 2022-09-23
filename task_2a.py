#  задача Баше
#2021 конфета
#2 игрока
#от 1 до 28 конфет за ход
#Все конфеты оппонента достаются сделавшему последний ход. 
# cколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random
candies=2021
candies_min=1
candies_max=28
key=candies_min+candies_max
print ('ключевое число: ',key)
b=candies/key
b=int (b)
c=b*key
first_step=candies-c
print ('если хочешь выиграть, на первом шаге бери',first_step)
print()
gaemers=["Игрок", "Бот" ]
start=(random.choice(gaemers))
print('первый ход за ', start)
if start=="Игрок":
  player=int(input ('Твой ход! сколько конфет возьмешь? '))
  bot=key-player
  print('бот взял ', bot, ' конфет')
  candies=candies-player-bot
  print('в игре ', candies, ' конфет')
  last_step="Бот"
  print()
elif start=="Бот":
  bot=first_step
  print('бот взял ', bot, ' конфет')
  player=int(input ('Твой ход! сколько конфет возьмешь? '))
  candies=candies-player-bot
  print('в игре ', candies, ' конфет')
  last_step="Игрок"
while candies>0:
  if last_step=="Бот":
    player=int(input ('Твой ход! сколько конфет возьмешь? '))
    candies=candies-player
    last_step="Игрок"
  elif last_step=="Игрок":
    bot=key-player
    print('бот взял ', bot, ' конфет')
    candies=candies-bot
    last_step="Бот"
  print('в игре ', candies, ' конфет')
  print()
  if candies==0:
   print('конфеты кончились') 
   print('победил ', last_step)





  


