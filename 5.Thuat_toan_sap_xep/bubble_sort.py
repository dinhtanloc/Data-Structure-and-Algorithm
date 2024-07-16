def bubble_sort(array):
    n = len(array)
   
    for step in range(n):

        for i in range(0, n-step-1):
         
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    
    return array

arr = [7, 2, 5, 4, 17]
bubble_sort(arr)