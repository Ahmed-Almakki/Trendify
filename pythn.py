# def summToTarget(arr, target):
#     num_dict = {}
#     for i, num in enumerate(arr):
#         complemnt = target - num
#         print(num_dict)
#         if complemnt in num_dict.keys():
#             return [num_dict[complemnt], i]
#         num_dict[num] = i
#     return []
# print(summToTarget([11, 7, 2, 15], 22))



# def pascalTraingle(n):
#     if n <= 0:
#         return []
#     lst = [[1] for i in range(n)]
#     count = 0
#     for row in lst:
#         if count >= 1:
#             for col in range(1, count):
#                 prevNumber = lst[count - 1][col - 1]
#                 currNumber = lst[count - 1][col]
#                 summ = prevNumber + currNumber
#                 row.append(summ)
#             row.append(1)
#         count += 1
#     return lst
# for x in pascalTraingle(5):
#     print(x)

#lock box
# def canUnlockAll(boxes):
#     unlockedBox = set()
#     stack = [0]
#     while stack:
#         # print(f"the stack {stack}\n unlockedBox {unlockedBox}")
#         current = stack.pop()
#         for key in boxes[current]:
#             if key not in unlockedBox:
#                 unlockedBox.add(key)
#                 stack.append(key)
#     return len(unlockedBox) == len(boxes)


# copy paste
# def minOperations(n):
#     operation = 0
#     div = 2
#     while n > 1:
#         while n % div == 0:
#             operation += div
#             n //= div
#         div += 1
#     return operation


# def rotate_2d_matrix(matrix):
#     n = len(matrix)
#     holder = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             holder[j][n-i-1] = matrix[i][j]
#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = holder[i][j]
#     print(holder)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# rotate_2d_matrix(matrix)


def makeChange(coins, total):
    sortCoin = sorted(coins)[::-1]
    if total == 0 or total < 0:
        return 0
    x = True
    i = 0
    lstCoint = []
    while total != 0 and i != len(sortCoin):
        if total >= sortCoin[i]:
            lstCoint.append(sortCoin[i])
            total -= sortCoin[i]
        else:
            i += 1
    if total != 0:
        return -1
    return len(lstCoint)

print(makeChange([1256, 54, 48, 16, 102], 1453))
print(makeChange([1, 2, 25], 37))