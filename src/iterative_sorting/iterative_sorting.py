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

# selection_sort([2, 9, 1, 2, 3, 6, 2, 12, 1])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop over every value in the array
    for i in range(len(arr)):
        # For every value, we want to move accross the rest of the array 
        # Until we reach the end or come accross a value that's larger than the current one
        for j in range(0, len(arr) - i - 1):
            # We want to check if the value to the right is smaller than the current value
            if arr[j] > arr[j+1]:
                print(f"\n{arr[j]} is larger than {arr[j+1]} and should be switched") 
                # Swap the two values
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # If no swap is performed, the array has been sorted
    return arr

# print(bubble_sort([3, 3, 1, 23, 12313, 91,319, 0, 19, 2, 10, 4, 2]))

# STRETCH: implement the Count Sort function below
# counting sort is based on keys between a specific range
# It works by counting the number of objects having distinct values.
def count_sort( arr, maximum=-1 ):
    # Create count list with the same length as the array, comprised of zero
    count = [0] * maximum
    
    # Loop over values in array
    for i in range(len(arr)):
        # For every instance of a number in the array, add a 1 to the respective position in count
        count[arr[i]] += 1
    
    # Modify count array so that each element at each index stores the sum of previous counts
    sum_of_counts = 0
    for i in range(len(count)):
        sum_of_counts = sum_of_counts + count[i]
        count[i] = sum_of_counts

    output = [0] * len(arr)
    for j in range(len(arr)):
        # Take value at arr[i]
        array_val = arr[j]

        # Get the designated position from the count list
        designated_position = count[arr[j]] - 1 # value of count of value arr[j]

        # Set array value to designated position
        output[designated_position] = array_val

        # Subtract 1 from the value of count
        count[arr[j]] -= 1
        
    return output

print(count_sort([3, 1, 7, 7, 2], 10))