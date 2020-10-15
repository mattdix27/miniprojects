import random
random_list = random.sample(range(1,1000000), 10000)

'''
Bubble sort
'''

def bubble_sort(num_list):
    while True:
        swapped = False
        for i in range(len(num_list)-1):
            if num_list[i] > num_list[i+1]:
                (num_list[i],num_list[i+1])=(num_list[i+1],num_list[i])
                swapped = True
        if swapped == False:
            break
    return num_list

'''
Merge sort
'''

def merge_sort(num_list):
    left = []
    right = []
    
    if len(num_list) <= 1:
        return num_list
    
    for i in range(len(num_list)):
        if i < (len(num_list))/2:
            left.append(num_list[i])
        else:
            right.append(num_list[i])
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left,right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result

print(merge_sort(random_list))
print(bubble_sort(random_list))