
secret_message = input('enter secret message:')
n = int(input('enter shift:'))

i = 0

f = open('Secret_Message.txt', 'w')

for i in range(len(secret_message)):
    

    x = ord(secret_message[i]) - n
    if x < 97:
        x = x + 26
    
    y = chr(x)
    print(y, end='')


    f.write(f'{y}')
f.close()

print('')

