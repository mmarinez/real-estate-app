import os


def main():
    print_header()
    filename = get_date_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-------------------------')
    print('     REAL ESTATE APP')
    print('-------------------------')
    print()


def get_date_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'Sacramentorealestatetransactions.csv')


def load_file(filename):
    return []


def query_data(data):
    pass


if __name__ == "__main__":
    main()