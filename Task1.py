# Напишите программу, удаляющую из
# текста все слова содержащие "абв".

text = 'Напишите  напишитеабв программу, удаляющую из \
    этого абв текста все слова, содерабващие содержащие "абв" "aбв".'

print(" ".join(list(filter(lambda x: 'абв' not in x, text.split()))))