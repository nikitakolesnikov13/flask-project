"""
X красных машин и Y белых стоят в одном ряду Напишите программу, которая выдаст, как нужно расположить красные и белые машины, чтобы рядом с каждой красной стояла хотя бы одна белая, а рядом с каждой белой — хотя бы одна красная.
На вход подаются два числа - кол-во красных машин X и кол-во белых машин Y. В ответе выведите какую-нибудь строку, в которой будет равно X символов “R” (красные машины) и Y символов “W” (белые машины), удовлетворяющую условию задачи. Пробелы между символами выводить не нужно. Если расставить машины согласно условию задачи невозможно, выведите строку “Нет решения”.

Задача основана на часто встречающейся задаче про кинотеатр и однолкссников

"""


red_cars = int(input('Введите кол-во красных машин: '))
white_cars = int(input('Введите кол-во белых машин: '))
answer = ''
if (red_cars > 2 * white_cars) or (white_cars > 2 * red_cars):
    print('Нет решения.')
elif red_cars >= white_cars:
    k = red_cars - white_cars
    for bgb in range(k):
        answer += '|Red|White|Red|'
    for bg in range(white_cars - k):
        answer += 'Red|White|'
else:
    k = white_cars - red_cars
    for gbg in range(k):
        answer += 'White|Red|White|'
    for gb in range(red_cars - k):
        answer += 'White|Red|'
print(answer)