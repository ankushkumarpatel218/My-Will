for i in range(2, 21):
    with open(f'table of {i}.txt', 'w') as table:
        for j in range(1, 11):
            mul = i*j
            table.write(str(i)+' X '+str(j)+' = '+str(mul)+'\n')