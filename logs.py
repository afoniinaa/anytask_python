import sys


def reading_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as file:
        for line in file:
            yield line.strip().split(',')


def most_popular_item(file_path: str, stat_type: str):
    stat_item = {}
    item = ''

    for line in reading_file(file_path):
        if stat_type == 'resource':
            item = line[13]
        elif stat_type == 'client':
            item = line[0]

        if item in stat_item.keys():
            stat_item[item] += 1
        else:
            stat_item[item] = 1

    for item, count in stat_item.items():
        if count == max(stat_item.values()):
            return item, count


def reading_parameters():
    if len(sys.argv) < 3:
        file_path = input("Enter path to file: ")
        stat_type = input("Enter type of statistics: ")
    else:
        file_path = sys.argv[1]
        stat_type = sys.argv[2]

    return file_path, stat_type


def result_func():
    args = reading_parameters()
    file_path = args[0]
    stat_type = args[1]
    result = most_popular_item(file_path, stat_type)
    print(f'The most popular {stat_type}: {result[0]}')
    print(f'Quantity: {result[1]}')


if __name__ == "__main__":
    result_func()
