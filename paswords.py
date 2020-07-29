#! python3
# paswords.py

PASWORDS = { 'email': 'vital2014','vk':'Vital2014','positive':'vital2014'}
import sys,pyperclip
if len(sys.argv)<2:
    print('Использование: python paswords.py[Имя учетной записи] - копирование пароля учетной записи')
    sys.exit()
account = sys.argv[1] # первый аргумент командной строки - это имя учетной записи

if account in PASWORDS:
    pyperclip.copy(PASWORDS[account])
    print ('Пароль для'+ account+'скопирован в буфер.')
else:
    print('Учетная запись'+account+'отсутствует в списке')