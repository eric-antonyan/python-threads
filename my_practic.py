import threading


def main():
    for i in range(1000):
        thread = threading.Thread(target=show_number, args=(i,))
        thread.start()


def show_number(number: int):
    print(number)


if __name__ == "__main__":
    main()
