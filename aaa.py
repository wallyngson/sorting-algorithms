def _sort(array):

    arr = array
    index = 0
    swapped = True

    while(swapped):
        swapped = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                _swap(arr, i, j)
                swapped = True
   
    print(array)
    
    def _swap(i, j):
        arr[j], arr[i] = arr[i], arr[j]
    
