#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

import re
import itertools
import os

text = 'WWWWWWWttttttDDDyyyyyRRRs'

with open('text_1.txt', 'w') as f:
    f.write(text)

with open('text_1.txt', 'r') as f:
    new_text = f.read()

def compress(x):
    for char, same in itertools.groupby(x):
        count = sum(1 for _ in same)
        yield char if count == 0 else str(count)+char

encode_txt = (''.join(compress(new_text)))

with open('encode_txt.txt', 'w') as data:
    data.write(encode_txt)

with open('encode_txt.txt', 'r') as data:
    decode = data.read()


def dec(y):
    f = re.findall(r'\d+', decode)
    f = [int(i) for i in f]

    s = re.findall(r'\D', decode)
    s = [i for i in s]

    x = ''.join([f[i]*s[i] for i in range(len(s))])
    return x

decode_text = (dec(decode))
print(decode_text)

with open('decode.txt', 'w') as f:
    f.write(decode_text)