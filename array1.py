# import array

# arr = [40,20,50,30,10]
# n = len(arr)
# print(arr)

# for i in range(n):
#     for j in range(n - 1- i):
#         if arr[j] > arr[j + 1]:
#             temp = arr[j]
#             arr[j] = arr[j + 1]
#             arr[j + 1] = temp
# print(arr)


#  Linear  search

# import array

# arr = [10,20,40,30,50]

# target = int(input("Enter Element = "))


# for i in arr:
#     if target == i:
#         print("Element found")
# else:
#         print("element not found")


arr = [10, 20, 30, 40, 50]

target = 40

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element Found")
        break

    elif target < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1