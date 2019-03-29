from random import random as random
import datetime
import sys
sys.setrecursionlimit(1000000)

# 선택정렬

def sort_selection(array):

    array = array[:]
    array2 = []

    for i in range(len(array)):
        num_max = 0
        for a in array:
            num_max = max(a, num_max)
        array2.insert(0, num_max)
        array.remove(num_max)

    return array2

 

# 버블소트

def sort_bubble(array):
    
    array = array[:]
    length = len(array)

    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    return array

 

# 삽입정렬

def sort_insertion(array):

    array = array[:]

    for i in range(1, len(array)):

        num = array[i]
        array.pop(i)
        
        for j in range(i):
            if num <= array[j]:
                break

        array.insert(j, num)

    num = array[i]
    array.pop(i)

    for j in range(i):
        if num <= array[j]:
            break

    array.insert(j if num <= array[j] else j+1, num)

    return array

 

# 합병정렬

def sort_merge(array):

    array = array[:]

    if len(array) == 1:
        return array

    index_half = int(len(array)/2)


    left = sort_merge(array[:index_half])
    right = sort_merge(array[index_half:])
    array = [0] * len(array)

    for i in range(len(array)):    

        if not len(left):
            array[i] = right.pop(0)
            continue 

        if not len(right):

            array[i] = left.pop(0)
            continue

        m = 0
        if left[0] < right[0]:
            m = left.pop(0)           

        else:
            m = right.pop(0)

        array[i] = m

    return array

    
def sort_heap(array):
    import heapq
    h = []
    for i in array:
        heapq.heappush(h, i)

    return list(heapq.heappop(h) for i in range(len(array)))
    
    
# 퀵 소트

# pivot = last, mid, random
def sort_quick_last(array):
    return sort_quick(array, 'last')

def sort_quick_mid(array):
    return sort_quick(array, 'mid')

def sort_quick_random(array):
    return sort_quick(array, 'random')

def sort_quick(array, pivot_id):
    
    array = list(array)
    size = len(array)

    if size < 2:
        yield from array
        return

    if pivot_id == "last":
        pivot = size - 1 

    elif pivot_id == "mid":
        pivot = sorted([0,-1,size//2],key = lambda x:array[x])[1]
    else:
        pivot = int(random() * size)

    num = array.pop(pivot)
    yield from sort_quick((a for a in array if a <= num), pivot_id)
    yield num
    yield from sort_quick((a for a in array if num < a), pivot_id)

# 랜덤한 배열 생성
def random_array(size):
    return [int(random()*size) for i in range(size)]

    
if __name__ == '__main__':
    arrays = [
        ('Random1000', random_array(1000)),
        ('Reverse1000', list(reversed(range(1000)))),
        ('Random10000', random_array(10000)),
        ('Reverse10000', list(reversed(range(10000)))),
        ('Random100000',random_array(100000)),
        ('Reverse100000',list(reversed(range(100000))))
    ]
    
    sorts = [
        ('Bubble',sort_bubble),
        ('Selection', sort_selection),
        ('Insertion', sort_insertion),
        ('Merge', sort_merge),
        ('Quick1', sort_quick_last),
        ('Quick2', sort_quick_mid),
        ('Quick3', sort_quick_random),
        ('Heap', sort_heap),
        ('Library', sorted),
    ]
    
    print('\t\t',end='')
    print(*('%10s'%name for name, array in arrays),sep='\t')

    for name_sort, sort in sorts:
        print('%10s'%(name_sort),end='\t')
        for name_array, array in arrays:
            time_start = datetime.datetime.now()
            try:
                list(sort(array[:]))
                elapsed_time = datetime.datetime.now() - time_start
                print('%10f'%elapsed_time.total_seconds(),end='\t')
            except MemoryError as e:
                
                print('%10s'%'MemoryError',end='\t')
            
        print()
 
