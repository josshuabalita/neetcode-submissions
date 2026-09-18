from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_new_list = []

    for sublist in nested_arr:
        max_in_list = sublist[0]
        for element in sublist:
            max_in_list = max(element, max_in_list)
        max_new_list.append(max_in_list)
    return max_new_list 

# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))

