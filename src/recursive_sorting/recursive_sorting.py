# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    # Loop over length of both combined lists
    for i in range(elements):
        # To handle cases where one of the arrays has already been emptied, check for length and work with the opposite
        if (len(arrA)) == 0:
            # Add ArrB[0] to merged_arr and remove it from ArrB
            merged_arr[i] = arrB[0]
            arrB.pop(0)

        elif (len(arrB)) == 0:
            # Add ArrA[0] to merged_arr and remove it from ArrA
            merged_arr[i] = arrA[0]
            arrA.pop(0)
    
        elif arrA[0] <= arrB[0]:
            # Add ArrA[0] to merged_arr and remove it from ArrA
            merged_arr[i] = arrA[0]
            arrA.pop(0)

        else:
            # Add ArrB[0] to merged_arr and remove it from ArrB
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    
    return merged_arr

# print(merge([1, 4], [5]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Base case
    if len(arr) == 1:
        return arr

    # Recursive case
    else:
        # Split the array into two


        # Run recursive on both halfs

        # return merge between the two


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
