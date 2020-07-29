import random

message=['Конечно да!',
'Скорее да чем нет',
'Скорее нет чем да',
'Конечно нет!']

print(message[random.randint(0,len(message)-1)])
print('Нажмите Enter для заверщения программы')
input()