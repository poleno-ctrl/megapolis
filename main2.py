def sort(ar):                                    #функция сортировки "пузырьком"
    for i in range(len(ar)):
        j = i
        while j >= 0 and ar[j][1] < ar[j-1][1]:
            t = ar[j]
            ar[j] = ar[j-1]
            ar[j-1]=t
            j-=1
    return ar

a = []

with open('astronaut_time.txt', encoding='utf-8') as f:        #чтение файла
    a = f.read().split()
inf = a[1:]                                                    #отбрасываем первую строчку с названиями стобцов
for i in range(len(inf)):
    inf[i] = inf[i].split('>')
inf = sort(inf)                                                #сортируем данные
with open('sorted.txt', 'w', encoding='utf-8') as f:           #запись в файл
    for i in range(3):
        f.write(f'На станции {inf[i][1]} в каюте {inf[i][2]} восстановлено время. Актуальное время: {inf[i][4]}\n')

