"""
A short implementation of some sorting algorithms...
"""

import numpy as np


class Sorter:
    def __init__(self):
        pass

    @staticmethod
    def _simple_1v1_model(array: np.ndarray or list) ->np.ndarray or list:
        """
        compares two elements and sets the biggest one forward;
        makes it repeatedly while no permutations are made;
        :param array or list
        :return: array or list
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
    def _simple_1v1_quicker_model(array: np.ndarray or list) ->np.ndarray or list:
        """
        quicker realisation of previous model;
        compares current element with previous one and swaps if previous is bigger;
        :param array or list
        :return: array or list
        """
        for index in range(1, len(array)):
            current_element = array[index]
            item_before = index - 1
            while item_before >= 0 and array[item_before] > current_element:
                array[item_before+1] = array[item_before]
                item_before -= 1
            array[item_before+1] = current_element
        return array

    def _quickest_model(self, array: np.ndarray or list) ->np.ndarray or list:
        """
        this realisation is based on Tony Hoare algorithm;
        :param array or list
        :return: array or list
        """
        if len(array) <= 1:
            return array
        else:
            items = [[], [], [], array[(len(array)//2)-2]]
            for number in array:
                if number > items[3]:
                    items[1].append(number)
                elif number < items[3]:
                    items[0].append(number)
                else:
                    items[2].append(number)
            return self._quickest_model(items[0]) + items[2] + self._quickest_model(items[1])

    def performer(self, array: np.ndarray or list, flag='1') ->np.ndarray or list:
        if flag == '1':
            return self._quickest_model(array)
        elif flag == '2':
            return self._simple_1v1_quicker_model(array)
        elif flag == '3':
            return self._simple_1v1_model(array)
