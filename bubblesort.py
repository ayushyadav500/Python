def  bubble(arr):
    swap = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] >arr[j+1]:
                swap = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = swap
                
