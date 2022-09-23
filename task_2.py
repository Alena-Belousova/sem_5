#  задача Баше
#2021 конфета
#2 игрока
#от 1 до 28 конфет за ход
#Все конфеты оппонента достаются сделавшему последний ход. 
# cколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
candies=2021
candies_min=1
candies_max=28
key=candies_min+candies_max
print ('ключевое число: ',key)
b=candies/key
b=int (b)
#print (b)
c=b*key
#print (c)
first_step=candies-c
print ('если хочешь выиграть, на первом шаге бери',first_step)


