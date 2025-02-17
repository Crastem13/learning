# Merge and Sort Two Lists

## Definition:
# This task involves taking two separate lists of elements, combining them into a single list,
# and then sorting the combined list in ascending order. The elements in the lists can be of any
# comparable type, such as integers, floats, or strings. The goal is to produce a single sorted list
# that contains all the elements from both input lists.

## Objective:
# Create a program that merges two lists and then sorts the merged list.

## Requirements:
# 1. Create a function called merge_and_sort that takes two parameters list1 and list2.
# 2. Merge the two lists into one.
# 3. Sort the merged list in ascending order.
# 4. Return the sorted, merged list.
# 5. Write a few test cases to demonstrate the functionality of your merge and sort function.

def merge_and_sort(list1:list, list2:list) -> list:
    """
    Merges and sorts the two lists provided in the arguments.

    Args:
        - list1 : list
        - list2 : list

    Returns:
        - list : The merged and sorted list
    """

    # check if the arguments are both lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Error: Both arguments should be lists!")
    
    # handle the empty lists or one of them being empty
    if not list1 and not list2:
        return list1
    
    if not list1:
        list2.sort()
        return list2
    
    if not list2:
        list1.sort()
        return list1
    
    # merge and sort the lists
    list1.extend(list2)
    list1.sort()

    return list1

    #----------------#
    # Optimized Code #
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Error: Both arguments should be lists!")

    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

    #----------------#

# Test Cases
print(merge_and_sort([1231, 22, 33], [43, 45, 63]))
print(merge_and_sort([1, 10, 13], [14, 52, 61]))
print(merge_and_sort(["one", "two", "four"], ["three", "nine", "six"]))
print(merge_and_sort([False, False, True], [True, False, True]))
print(merge_and_sort([(3,4,5), (2,3)], [(1,3), (3,5,6,7)])) 

# Positives:
# 1. Function Definitions: Clear and concise function definitions with proper docstrings.
# 2. Error Handling: Proper error handling for non-list inputs.
# 3. Logic: The logic to merge and sort the lists is well-implemented.
# 4. Test Cases: Including test cases with diverse data types to demonstrate functionality is excellent.

# Suggestions for Improvement:
# 1. Returning Value Errors: Instead of returning a ValueError, you should raise it:
# if not isinstance(list1, list) or not isinstance(list2, list):
#    raise ValueError("Error: Both arguments should be lists!")

# 2. Simplifying Sorting Logic: Instead of sorting each list individually when one is empty, you can merge 
# the lists first and then sort the combined list:
#
# if not isinstance(list1, list) or not isinstance(list2, list):
#         raise ValueError("Error: Both arguments should be lists!")
# 
#     merged_list = list1 + list2
#     merged_list.sort()
#     return merged_list

# 3. Returning Empty List: Ensure the function handles cases where both lists are empty correctly.