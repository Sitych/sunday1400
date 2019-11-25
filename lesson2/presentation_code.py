# Одиночные кавычки. Часто встречаемый вариант записи.my_str = 'а внутри "можно" поместить обычные‘
my_str = "а внутри 'можно' " + " поместить одиночные"

example_string = "Курс по Python"
print(example_string)

print(type(example_string))

S1 = 'Py'
S2 = 'thon'
S3 = S1 + S2
print(S3)
print(S3 * 4)

S = 'Python'
SubS = 'th'
# pritn(SubS in S)

S = 'Python'
print(S [0])
print(S[ -1])

S = 'Ура'
# S[1] = 'х'
print(S [0]+ 'x' +S[2])

f = open('filename', 'w')
f.write('The world is changed.\nI taste it in the water.\n')
f.close()
f = open('filename', 'r+')
print(f.read())
print(f.tell())

f = open('filename', 'r+')
print(f.readline())
f.close()

with open('filename') as f:
    print(f.read())
