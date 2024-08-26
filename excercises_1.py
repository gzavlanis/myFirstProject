import re, string, random, itertools

def SimpleAdding(num):
    x = 0
    for i in range(0, num + 1):
        x += i
    return x

# print(SimpleAdding(int(input())))

def CheckNums(num1, num2):
    if num1 < num2:
        x = "True"
    elif num1 == num2:
        x = -1
    else:
        x = "False"
    return x

# print(CheckNums(int(input()), int(input())))

def FirstReverse(strParam):
    strParam = strParam[::-1]
    return strParam

# print(FirstReverse(input()))

def FirstFactorial(num):
    factorial = 1
    if num != 0:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial

# print(FirstFactorial(int(input())))

def LetterCapitalize(strParam):
    strParam = string.capwords(strParam)
    return strParam

# print(LetterCapitalize(input()))

def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    return f"{hours}:{minutes}"

# print(TimeConvert(int(input())))

def VowelCount(strParam):
    count = 0
    vowels = ['a','e','i','o','u']
    for x in strParam.lower():
        if x in vowels:
            count += 1
    return count

# print(VowelCount(input()))

def WordCount(strParam):
    return len(strParam.split())

# print(WordCount(input()))

def LongestWord(sen):
    pattern = re.compile(r'[a-zA-Z0-9]+')
    words = re.findall(pattern, sen)
    longest = words[0]
    for i in range(1, len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    return longest

# print(LongestWord(input()))

def SimpleSymbols(strParam):
    if strParam[0].isalpha() or strParam[-1].isalpha():
        return "false"
    for char in range(1, len(strParam) - 1):
        if strParam[char].isalpha():
            if strParam[char - 1] == "+" and strParam[char + 1] == "+":
                pass
            else:
                return "false"
    return "true"

# print(SimpleSymbols(input()))

def AlphabetSoup(strParam):
    return "".join(sorted(strParam))

# print(AlphabetSoup(input()))

def ABCheck(strParam):
    return "true" if re.search(r'a...b|b...a', strParam) else "false"

# print(ABCheck(input()))

def ExOh(strParam):
    return True if strParam.count("x") == strParam.count("o") else False

# print(ExOh(input()))

def Palindrome(strParam):
    mystring = strParam.replace(" ", "")
    return mystring == mystring[::-1]

# print(Palindrome(input()))

def LargestPair(num):
    num = str(num)
    double_digits = []
    for k, i in enumerate(num):
        if k < len(num) - 1:
            a = i + num[k + 1]
            double_digits.append(a)
    max_number = max(double_digits)
    return max_number

# print(LargestPair(input()))

def NonrepeatingCharacter(strParam):
    string = list(strParam)
    for char in string:
        if char.isalpha():
            count = string.count(char)
            if count == 1:
                return char

# keep this function call here
# print(NonrepeatingCharacter(input()))

def TwoSum(arr):
    s = int(arr[0])
    arr = arr[1:]
    res = []
    for idx, i in enumerate(arr):
        for j in arr[idx:]:
            if i + j == s:
                res.append(f'{i},{j}')
    return " ".join(res) if res else -1

# print(TwoSum(input()))

def BitwiseTwo(strArr):
    first = strArr[0]
    second = strArr[1]
    new_string = ""
    for k, i in enumerate(first):
        if (i == '1') and (second[k] == '1'):
            new_string += "1"
        else:
            new_string += "0"
    return new_string

# print(BitwiseTwo(input()))

def PowerSetCount(arr):
    leng = len(arr)
    number_of = 1
    for i in range(1, leng+1):
        number_of = (number_of * 2)
    return number_of

# print(PowerSetCount(input()))

def ProductDigits(num):
    if num < 10:
        return 2
    min_v = len(str(num)) + 1
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i * j == num:
                v = len(str(i) + str(j))
                if min_v > v:
                    min_v = v
    return min_v

# print(ProductDigits(int(input())))

def PalindromeCreator(strParam):
    def is_palindrome(v):
        return v == v[::-1]

    if is_palindrome(strParam):
        return 'palindrome'

    for i in range(len(strParam)):
        v = strParam[:i] + strParam[i + 1:]
        if is_palindrome(v) and len(v) > 2:
            return strParam[i]

    for i in range(len(strParam)):
        for j in range(i + 1, len(strParam)):
            v = strParam[:i] + strParam[i + 1:j] + strParam[j + 1:]
            if is_palindrome(v) and len(v) > 2:
                return strParam[i] + strParam[j]

    return 'not possible'

# print(PalindromeCreator(input()))

def BasicRomanNumerals(strParam):
    # Dictionary with the values of Roman numerals
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Variable to store the final result
    total = 0
    # Variable to store the previous value
    prev_value = 0

    # Traverse the string from left to right
    for char in strParam:
        # Get the value of the current character
        current_value = roman_values[char]

        # If the current value is greater than the previous one, we need to subtract the previous from the result
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        # Update the previous value
        prev_value = current_value
    return total

# print(BasicRomanNumerals(input()))

def ThreeSum(arr):
    sum_to_reach = arr[0]
    arr = arr[1:]
    arr.sort()

    for i in range(0, len(arr) - 2):
        l = i + 1
        r = len(arr) - 1
        while (l < r):
            if (arr[i] + arr[l] + arr[r]) == sum_to_reach:
                return 'true'
            elif (arr[i] + arr[l] + arr[r]) < sum_to_reach:
                l += 1
            else:
                r -= 1
    return 'false'

# print(ThreeSum(input()))

def CorrectPath(s):
    while True:
        route = []
        tracepos = []
        x = 1
        y = 5
        answer = 1

        for i in s:
            if i == "?":
                i = random.choice("lrud")
            if i == "u":
                y += 1
            elif i == "d":
                y -= 1
            elif i == "r":
                x += 1
            elif i == "l":
                x -= 1

            if (x, y) in tracepos:
                answer = 0
                break
            else:
                tracepos.append((x, y))
            route.append(i)

            if x == 6 or x == 0 or y == 0 or y == 6:
                answer = 0
                break

        if x == 5 and y == 1 and answer == 1:
            return "".join(route)

# print(CorrectPath(input()))

def ScaleBalancing(strArr):
    x = list(int(s) for s in strArr[0][1:-1].split(','))
    y = list(int(s) for s in strArr[1][1:-1].split(','))
    # one
    for a in y:
        if x[0] + a == x[1] or x[1] + a == x[0]:
            return str(a)
    # two
    for pair in itertools.combinations(y, 2):
        if x[0] + pair[0] == x[1] + pair[1] or x[0] + pair[1] == x[1] + pair[0] or x[0] + pair[0] + pair[1] == x[1] or x[1] + pair[0] + pair[1] == x[0]:
            return ''.join(str(min(pair)) + ',' + str(max(pair)))
    return "not possible"

# print(ScaleBalancing(input()))

def ThreeNumbers(strParam):
    for word in strParam.split(' '):
        ints = set()
        for l in word:
            if l.isnumeric():
                ints.add(l)
        if len(ints) != 3 or "".join(ints) in word:
            return 'false'
    return 'true'

# print(ThreeNumbers(input()))

def AlphabetSearching(str):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in str:
        if i in alpha:
            alpha.remove(i)
    if len(alpha) == 0:
        return "true"
    else:
        return "false"

# print(AlphabetSearching(input()))

def TimeDifference(strArr):
    def convert_to_minutes(time_str):
        time_str = time_str.lower()  # Convert to lowercase for consistent handling
        h, m = map(int, time_str[:-2].split(':'))
        if 'pm' in time_str and h != 12:
            h += 12
        if 'am' in time_str and h == 12:
            h = 0
        return h * 60 + m

    # Step 1: Convert times to minutes
    times_in_minutes = [convert_to_minutes(time_str) for time_str in strArr]

    # Step 2: Sort the list of times in ascending order
    times_in_minutes.sort()

    # Step 3: Calculate the difference between adjacent times
    smallest_difference = float('inf')
    for i in range(1, len(times_in_minutes)):
        difference = times_in_minutes[i] - times_in_minutes[i - 1]
        if difference < smallest_difference:
            smallest_difference = difference

    # Check the difference between the first and last time (across the 12-hour boundary)
    difference = (times_in_minutes[0] + 24 * 60) - times_in_minutes[-1]
    if difference < smallest_difference:
        smallest_difference = difference

    # Step 4: Return the smallest difference in minutes
    return smallest_difference

# print(TimeDifference(input()))

def TriangleRow(num):
    if num == 0:
        return 1
    row = []
    for i in range(num):
        row = [1] + [a + b for a, b in zip(row[:-1],row[1:])] + [1]
    return sum(row)

# print(TriangleRow(int(input())))

def SimpleEvens(num):
    count_of_even = 0
    for number in str(num):
        if int(number) % 2 == 0:
            count_of_even += 1
    if count_of_even == len(str(num)):
        return 'true'
    else:
        return 'false'

# print(SimpleEvens(int(input())))