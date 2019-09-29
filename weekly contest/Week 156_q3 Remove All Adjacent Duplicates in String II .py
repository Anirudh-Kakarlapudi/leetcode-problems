"""
This script defines a :class: `Duplicates`, which implements k duplicate
removal in a string with methods :func: `remove_duplicates`, :func:
`delete_duplicates` and func: `index_finder`

Author:
----------
Anirudh Kumar Maurya Kakarlapudi
"""
from collections import OrderedDict


class Duplicates:
    """A class with :func:`remove_duplicates`, :func:`removeDupicates`,
    :func:`index_finder` to find all occurrences of the duplicates and to
    find the string without any duplicates of length k
    """
    def remove_duplicates(self, s: str, k: int) -> str:
        """Removes all the duplicates iteratively.

            Args:
              s: string from which duplicates are to be removed
              k: Number of duplicate removals

            Returns:
              The string without all the duplicates.
        """
        present = s
        remov = self.delete_duplicates(present, k)
        while(present != remov):
            present = remov
            remov = self.delete_duplicates(remov, k)
        return present

    def delete_duplicates(self, string: str, k: int) -> str:
        """Removes the duplicate in the string.

            Args:
              s: string from which duplicates are to be removed
              k: Number of duplicate removals

            Returns:
              The string without the duplicates.
        """
        # String(str1) contains the single occurrences of all characters
        # in string in same order as in string
        str1 = "".join(OrderedDict.fromkeys(string))
        for s1 in str1:
            # ind_list contains all the indexes of the letter 's1' in string
            ind_list = self.duplicates(list(string), s1)
            for ind in ind_list:
                # key is the sequence of 's1' occuring k times consequently
                key = s1*k
                # Delete the occurrence of 's1' k times consequently
                if(string[ind:ind+k] == key):
                    string = string[0:ind] + string[ind+k:]
        return string

    def index_finder(self, lst, element):
        """Removes the duplicate in the string.

            Args:
              lst: list in which indices are to be found
              element: an element whose index is to be found

            Returns:
              The list of all indices of element in a lst.
        """
        return [i for i, x in enumerate(lst) if x == element]
