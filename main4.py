#Python
with open('astronaut_time.txt', encoding='utf-8') as f:        #чтение файла
    a = f.read().split()
inf = a[1:]                                                    #отбрасываем первую строчку с названиями стобцов
ans1 = 0
ans2 = 0
for i in range(len(inf)):
    inf[i] = inf[i].split('>')
    inf[i][3] = ''.join(inf[i][3].split(':'))
    if inf[i][3] >= '000000' and inf[i][3] <= '120000':       #смотрим к какой группе отнести станцию
        ans1+=1
    else:
        ans2+=1
with open('stay.txt', 'w', encoding='utf-8') as f:            #запись в файл
    f.write(f'{ans1} станций остановилось с период с 00.00 до 12.00.\n')
    f.write(f'{ans2} станций остановилось с период с 12.01 до 23.59.')

