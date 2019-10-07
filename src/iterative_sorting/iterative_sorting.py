# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # Index of the smallest item in the array
        smallest_index = cur_index

        print(f"Current Index: {cur_index}\nSmallest index: {smallest_index}")

        # Loop over all values between i (cur_index) and len(arr)
        for j in range(cur_index, len(arr)):
            # If value at current location < previously smallest_index
            if arr[j] < arr[smallest_index]:
                # Set smallest_index to current location (j)
                smallest_index = j

        # Once smallest_index is known (since it loops over the entirety of the array)
        # Swap the indexes of the two values so the smallest is in the correct position
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

        print(f"Array: {arr}\n")

    return arr

selection_sort([2, 9, 1, 2, 3, 6, 2, 12, 1])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr