import sys


def main(argv):
    print("Welcome to gnurr!")

    read_commands(argv)

    print("Programmed by Arden Raaen.\n")


def read_commands(items_list):
    f = open('out.txt', 'w')

    for n in range(0, len(items_list)):
        print(items_list[n])
        f.write(items_list[n] + '\n')


if __name__ == "__main__":
    main(sys.argv)
