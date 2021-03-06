# Описание решения:
# У нас есть шахматная квадратная доска произвольного размера
# Создаем функцию с параметрами x - это номер столбца, у - это номер строки, n - размер доски,
# n - кол-во путей пройти в дамку, для каждого "плеча" рекурсивной функции - значение всегда 1
# так как одно плечо - один путь
# в конечном итоге количество плеч сумируется
# далее коментариии напротив строк кода
import time

def count_ways(x, y, size, n):
    """
        Данная функиця определяет количество путей пройти в дамки
        x - номер столбца от 0 до n-1
        y - номер строки от 0 до n-1
        size - размер доски, доска квадратная
        n - кол-во вариантов пройти в дамки у каждого плеча один вариант, n = 1 всегда
    """
    if y == size - 1:  # если достигли вершины доски - выходим из рекурсии и отдаем число варианов n = 1
        return n

    if x == 0:  # если шашка находится в крайнем левом столбце - возможна только одна ветвь
        return count_ways(1, y + 1, size, n)  # переходим на следующую строку и отодвигаемся от края вправо (0+1)

    if x == size - 1:  # если шашка находится в крайнем правом столбце - возможна только одна ветвь
        return count_ways(size - 2, y + 1, size, n)
        # переходим на следующую строку и отодвигаемся от края влево (size - 2)

    # если же шашка не на краю, вариантов два, можно двигаться вправо x+1 или влево x-1, вверх только y + 1
    # так как пути два получаем сумму двух вариантов
    return count_ways(x + 1, y + 1, size, n) + count_ways(x - 1, y + 1, size, n)


if __name__ == '__main__':
    print(count_ways(6, 0, 13, 1)) # выводим количестов путей, шашка стоит в середине первой строки
    time.sleep(10) # ждем 10 секунд чтобы посмотреть результат
