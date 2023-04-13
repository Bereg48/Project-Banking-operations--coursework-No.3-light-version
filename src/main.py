from utils import load_operations, filter_data, sort_data, format_data


def main():
    data = load_operations()
    data = filter_data(data)
    data = sort_data(data)
    data = format_data(data)

    for row in data:
        print(row)


if __name__ == "__main__":
    main()
