import sys
import random

password = 'senha'

table_ascii = []
table_crypt = []

alfanum = 'ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuVwyxz0123456789 '

# vamos utilizar a tabela ASCII
#for n in range(128):
#    ch = chr(n)

# vamos utilizar somente os caracteres do alfanum
for n in range(len(alfanum)):
    ch = alfanum[n]
    table_ascii.insert(n, ch)
    table_crypt.insert(n, ch)

random.seed(password)
random.shuffle(table_crypt)


source = 'abcde'
dest   = ''
print('=> source word: ' + source)

len = len(source)
for n in range(len):
    ch = source[n]
    print('=> source char: ' + ch)
    pos = table_ascii.index(ch)
    cr  = table_crypt[pos]
    print('=> crypto char: ' + cr)
    dest += cr

print('=> dest word: ' + dest)