def symma_nechetnih(m_number):
    spisok = [int(i) for i in range(1, m_number + 1)]
    s = 0
    for i in range(len(spisok)):
        if spisok[i] % 2 == 1:
            s += spisok[i]
    return s

data = int(input('Пожалуйста, введите верхнюю границу количества чисел в списке: '))
print(f'Сумма всех нечётных чисел в заданном диапазоне: {symma_nechetnih(data)}')