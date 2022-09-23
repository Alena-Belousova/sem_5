# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open('C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\19.09\\read_4.txt') as d:
 data=d.read()
 print(data)
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
           if prev_char:
              encoding += str(count) + prev_char
           count = 1
           prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding 
encoded_val = rle_encode(data)
print(encoded_val)
file = open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\19.09\\write_4.txt", "w")
file.write(encoded_val)
file.close()


