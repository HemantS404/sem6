import random
import time

data = [random.randint(1, 10000) for _ in range(1, 100)]
print("Before:", data, end='\n\n')
# data = [random.randint(1, 1000) for i in range(15, -1, -1)]
n = len(data)

def partition(low, high):
    # # Houre
    # pivot = random.randint(low, high)
    # data[pivot], data[low] = data[low], data[pivot]

    # pivot = low
    # i = low
    # j = high

    # while(i < j):
    #     while(i < high and data[i] <= data[pivot]): i+=1
    #     while(j > low and data[j] > data[pivot]): j-=1
    #     if (i < j):
    #         data[j], data[i] = data[i], data[j]
    #     else:
    #         break
    
    # data[j], data[pivot] = data[pivot], data[j]

    # Lomoto
    pivot = random.randint(low, high)
    data[pivot], data[high] = data[high], data[pivot]

    pivot = high
    i = low
    j = high

    while(i < j):
        while(i < high and data[i] <= data[pivot]): i+=1
        while(j > low and data[j] > data[pivot]): j-=1
        if (i < j):
            data[j], data[i] = data[i], data[j]
    
    data[j], data[pivot] = data[pivot], data[j]
    
    return j


def quickSort(low, high):
    if low >= high:
        return
    else:
        k = partition(low, high)
        quickSort(low, k-1)
        quickSort(k+1, high)

start = time.time_ns()
quickSort(0, n-1)
end = time.time_ns()

print("After : ", data, end='\n\n')
print(f"Time taken in milisec : {(end - start)/1000}")