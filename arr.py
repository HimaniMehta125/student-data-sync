# import array

# # one Dimensional Array

# arr = array.array('i',[1,2,3,4])
# print(arr)
# arr.append(5)
# print(arr)
# arr.append(6)
# print(arr)
# arr.remove(6)
# print(arr)

# #  tow Dimensional Array


# arre = [
#     [10, 20, 30, 40],
#     [60, 70, 80, 90]
# ]

# print(arre)

# arre.append([50,100])

# print(arre)

# arre.pop()
# print(arre)

# #  multi Dimensional array

# arrh = [

#             [

#                 [1,1],
#                 [2,2]

#             ],

#             [
#                 [3,3],
#                 [4,4]

#             ]

# ]

# print(arrh)
# arrh.append([6,6])
# print(arrh)

import array

arra = [
        [1,2,3,4,5],
        [6,7,8,9,10]
]

for row in arra:

    for col in row: 
        print(col,end=" ")

    print(col)