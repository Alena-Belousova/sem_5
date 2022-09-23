#   Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text='мой дядя абвсамых абвчестных абвправил, когдаабв неабв абвшутку занемог...'
#print('исходник: ',text)
words = text.split(' ')
#print(words)
fragment = 'абв'
new_text = []
for word in words:
    if fragment not in word:
      new_text.append(word)
      result_text= ' '.join(new_text)
print('результат: ', result_text)




