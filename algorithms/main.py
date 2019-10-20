"""
A short implementation of some sorting algorithms...
"""

import numpy as np


class Sorter:
    def __init__(self):
        pass

    @staticmethod
    def simple_1v1_model(array: np.ndarray or list) ->np.ndarray or list:
        """
        compares two elements and sets the biggest one forward;
        makes it repeatedly while no permutations are made;
        :param array
        :return: array
        """
        flag = True
        while flag:
            flag = False
            for index in range(0, len(array)-1):
                if array[index] > array[index+1]:
                    array[index], array[index+1] = array[index+1], array[index]
                    flag = True
        return array

    @staticmethod
    def simple_1v1_quicker_model(array: np.ndarray or list) ->np.ndarray or list:
        """
        quicker realisation of previous model;
        compares current element with previous one and swaps if previous is bigger;
        :param array
        :return: array
        """
        for index in range(1, len(array)):
            current_element = array[index]
            item_before = index - 1
            while item_before >= 0 and array[item_before] > current_element:
                array[item_before+1] = array[item_before]
                item_before -= 1
            array[item_before+1] = current_element
        return array

    @staticmethod
    def quickest_model(array: np.ndarray or list) ->np.ndarray or list:
        """
        this realisation is based on Tony Hoare algorithm;
        :param array: 
        :return:
        """
        pass
