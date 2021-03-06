# Program SEARCH1 in Python
# Figure 2.2 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def search1(set, data):
    """
    Search for a given element in a set
    :param set: set to search in
    :param data: data to search for
    """

    n = len(set)                        # n is the number of elements of set

    i = 0
    while i <= n - 1:
        if set[i] == data:
            print "%s is present" % data
            return
        else:
            i = i + 1

    print "%s is not present" % data


def main():

    city = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']

    search1(city, 'NA')

    search1(city, 'RC')


if __name__ == "__main__":
    main()
