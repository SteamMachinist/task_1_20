# (*) Вернуть в виде списка самую длинную подпоследовательность подряд идущих чисел, сумма которых максимальна
# (задача имеет смысл, если в исходной последовательности будут встречаться, как положительные, так и отрицательные
# элементы). Если таких последовательностей несколько с одинаковой длиной, то вернуть первую (от начала списка) такую
# подпоследовательность. Реализовать поиск такой подпоследовательности в один проход (один цикл, второй цикл будет
# использоваться для копирования элементов найденной подпоследовательности в результирующий список).

def read_list_from_file(filepath):
    file = open(filepath, 'r')
    list = [int(x) for x in file.read().strip().split(" ")]
    file.close()
    return list


def write_list_to_file(filepath, list: list):
    file = open(filepath, 'w')
    file.write(" ".join([str(x) for x in list]))
    file.close()


def find_max_sum_longest_sublist(initial_list: list):
    start = 0
    length = 1
    for n in range(len(initial_list)):
        pass
    return [initial_list[x] for x in range(start, start + length)]


if __name__ == '__main__':
    write_list_to_file("output/output1.txt", find_max_sum_longest_sublist(read_list_from_file("input/input1.txt")))
