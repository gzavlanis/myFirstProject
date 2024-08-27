import re

def LCS(strArr):
    # Extract the two strings from the input array
    str1, str2 = strArr

    # Initialize a table to store the LCS for substrings
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Fill the table using dynamic programming
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the length of the LCS for the entire strings
    return dp[-1][-1]

# print(LCS(input()))

def KaprekarsConstant(num):
    if len(str(num)) < 4:
        num = num * 10 ** (4 - len(str(num)))
    ascList = list(map(str, str(num)))
    desList = list(map(str, str(num)))
    ascList.sort()
    desList.sort(reverse = True)
    number = int(''.join(desList)) - int(''.join(ascList))
    if number == 6174:
        return 1
    else:
        return 1 + KaprekarsConstant(number)

# print(KaprekarsConstant(int(input())))

def find_partition(arr, curr_index, set1, set2):
    if curr_index == len(arr):
        # Check if both sets have the same sum
        if sum(set1) == sum(set2):
            return set1, set2
        return None

    # Try adding the current element to set1
    new_set1 = set1 + [arr[curr_index]]
    result = find_partition(arr, curr_index + 1, new_set1, set2)
    if result:
        return result

    # Try adding the current element to set2
    new_set2 = set2 + [arr[curr_index]]
    result = find_partition(arr, curr_index + 1, set1, new_set2)
    if result:
        return result

    return None


def ParallelSums(arr):
    result = find_partition(arr, 0, [], [])
    if result:
        # Sort both sets in ascending order and concatenate them into a comma-separated string
        return ','.join(map(str, sorted(result[0]))) + ',' + ','.join(map(str, sorted(result[1])))
    else:
        return -1

# print(ParallelSums(input()))

def ChessboardTraveling(str):
    # Use regular expression to extract the coordinates from the input string
    pattern = r"\d+"
    coords = list(map(int, re.findall(pattern, str)))
    x1, y1, x2, y2 = coords

    # Define the recursive function to count the number of ways
    def count_ways(x, y):
        if x == x2 and y == y2:
            return 1
        if x > x2 or y > y2:
            return 0
        return count_ways(x + 1, y) + count_ways(x, y + 1)

    return count_ways(x1, y1)

# print(ChessboardTraveling(input()))