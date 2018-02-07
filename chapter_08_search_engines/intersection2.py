# Program INTERSECTION2 in Python
# Figure 8.6 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import math


def intersection2(a, b):
    """
    Prints all the elements of vector a which are contained also in vector b.
    The search of each element b[k] in a is performed by means of the algorithm BINARY_SEARCH on a 
    copied and adapted here for printing the right elements. 
    Vector b can be not sorted because all its elements are sequentially examined.
    :param a: sorted vector a of n elements
    :param b: vector b of m elements (not necessarily sorted)
    """

    n = len(a)
    m = len(b)

    for k in range(0, m):
        i = 0
        j = n - 1
        while i <= j:
            c = int(math.floor((i + j) / 2))
            if b[k] == a[c]:
                print b[k]
                break              # the break command exit from the while loop
            elif b[k] < a[c]:
                j = c - 1
            else:
                i = c + 1


def main():

    torre = [9, 11, 15, 21, 27, 89, 101, 150, 500, 800, 811]    # vector a is sorted
    pisa = [9, 1, 3, 144, 210]                                  # vector b is not necessarily sorted

    intersection2(torre, pisa)


if __name__ == "__main__":
    main()