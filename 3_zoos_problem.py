word = input()

#convert word into list
word_list = list(word)

#get the specific occurrence
z_count = word_list.count('z')
o_count = word_list.count('o')

if 2 * z_count == o_count:
    print('Yes')
else:
    print('No')