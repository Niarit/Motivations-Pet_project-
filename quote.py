import random
import prints


def read_file(file_name):
    datas = []
    with open("file_name", "r") as f:
        for line in f:
            datas.append(line)
    return datas


def choose_random_quote(file_name):
    quote_list = read_file(file_name)
    random.choice(quote_list)
