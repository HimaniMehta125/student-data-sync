# import array


# bubble short

# arr = [5,3,4,1,2]                       
# n = len(arr)
# print(arr)
# print(n)

# for i in range(n):
#     for j in range(n - 1):
#         if arr[j]  > arr[j + 1]:
#             arr[j],arr[j + 1] = arr[j + 1],arr[j]

# print(arr)

# selection short

# arr =  [5,4,3,2,1]

# n = len(arr)

# for  i in range(n):
#     min_index = i

#     for j in range(i+1,n):

        
#         if arr[j] < arr[min_index]:

#             min_index = j

#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)

# #  insert shorting

# arr = [5, 2, 4, 1]

# for i in range(1, len(arr)):

#     key = arr[i]
#     j = i - 1

#     while j >= 0 and key < arr[j]:

#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key

# print(arr)

# marge short

# def merge_sort(arr):

#     if len(arr) > 1:

#         mid = len(arr) // 2

#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):

#             if left[i] < right[j]:

#                 arr[k] = left[i]
#                 i += 1

#             else:

#                 arr[k] = right[j]
#                 j += 1

#             k += 1

#         while i < len(left):

#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):

#             arr[k] = right[j]
#             j += 1
#             k += 1


# arr = [5, 2, 4, 1]

# merge_sort(arr)

# print(arr)

#  Quick Sort

# def quick_sort(arr):

#     if len(arr) <= 1:
#         return arr

#     pivot = arr[0]

#     left = [x for x in arr[1:] if x <= pivot]
#     right = [x for x in arr[1:] if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# arr = [5, 2, 4, 1]

# print(quick_sort(arr))