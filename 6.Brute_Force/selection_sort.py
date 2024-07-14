def selection_sort(array):
    n = len(array)
   
    for step in range(n):
        min_idx = step

        for i in range(step + 1, n):
         
            if array[i] < array[min_idx]:
                min_idx = i
            
        array[step], array[min_idx] = array[min_idx], array[step]
    
    return array

arr = [7, 2, 5, 4, 17]
selection_sort(arr)