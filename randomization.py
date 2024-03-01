import random


def randomize_array(array):
    """
    Randomize the order of elements in the given array.
    :param array: The input array to be randomized.
    :return: A new array with elements in random order.
    """
    randomized_array = array.copy()
    random.shuffle(randomized_array)
    return randomized_array
