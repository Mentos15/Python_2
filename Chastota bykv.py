import pprint
message = 'Вчера на улице было намного холоднее чем сегодня'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(pprint.pformat(count))