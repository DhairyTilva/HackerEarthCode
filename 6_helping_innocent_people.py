tag = input()

def is_even(n1,n2):
    if (int(n1) + int(n2)) % 2 == 0:
        return True
    return False

if tag[2] in ['A','E','I','O','U','Y']:
    print('invalid')
elif is_even(tag[0],tag[1]) and is_even(tag[3],tag[4]) and is_even(tag[4],tag[5]) and is_even(tag[7],tag[8]):
    print('valid')
else:
    print('invalid')