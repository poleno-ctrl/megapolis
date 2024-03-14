#Python
import sys
with open('astronaut_time.txt', encoding='utf-8') as f:        #чтение файла
    a = f.read().split()
inf = a[1:]                                                    #отбрасываем первую строчку с названиями стобцов
for i in range(len(inf)):
    inf[i] = inf[i].split('>')
while True:
    a = sys.stdin.readline().strip()
    if a == 'none':
        break
    f = 0
    for i in inf:
        if i[2]==a:
            sys.stdout.writelines(f'В каюте {i[2]} восстановлено время (время остановки: {i[3]}). Актуальное время: {i[4]}\n')
            f = 1
            break
    if f==0:
        sys.stdout.writelines('В этой каюте все хорошо\n')
