numbers = ['0','1','2','3','4','5']
acumulador =''
print('************************************')
for x in range(6):
    acumulador +=numbers[x]
    print(acumulador)
for y in range(5):
    print(acumulador[0:5-y])
print('************************************')
