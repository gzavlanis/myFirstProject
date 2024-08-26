import string

def PalindromeTwo(a_string):
    punctuation = string.punctuation
    no_spaces_string = a_string.replace(" ", "").lower()
    no_punct_string = ''
    for char in no_spaces_string:
        if char in punctuation:
            continue
        else:
            no_punct_string += char
    return no_punct_string == no_punct_string[::-1]

# print(PalindromeTwo(input()))

def Division(num1, num2):
    high = 1
    if num1 >= num2:
        size = num1
    else:
        size = num2
    for x in range(1, size):
        if (num1 % x == 0) and (num2 % x == 0) and (x > high):
            high = x
    return high

# print(Division(int(input()), int(input())))

def StringScramble(str1, str2):
    o_string = str1
    i_string = str2
    for char in i_string:
        if char not in o_string:
            return False
        updated_outer = o_string.replace(char, "", 1)
        o_string = updated_outer
    return True

# print(StringScramble(input(), input()))

def ArithGeoII(arr):
    # code goes here
    arithmetic = True
    d = arr[0] - arr[1]
    for i in range(1, len(arr) - 1):
        if arr[i] - arr[i + 1] != d:
            arithmetic = False
            break
    if arithmetic:
        return 'Arithmetic'

    geo = True
    r = arr[0] / arr[1]
    for i in range(1, len(arr) - 1):
        if arr[i] / arr[i + 1] != d:
            geo = False
            break
    if geo:
        return 'Geometric'

    return -1

# print(ArithGeoII(input()))

def BinaryConverter(str):
    return int(str, 2)

# print(BinaryConverter(input()))

def LetterCount(str):
    greatest = "-1"
    greatestCount = 0;

    def findRepeats(word):
        storage = {}
        rep = 0
        for letter in list(word):
            try:
                storage[letter] = storage[letter] + 1
            except:
                storage[letter] = 1
        for n in storage:
            if storage[n] > 1:
                rep = rep + storage[n]
        return rep

    arr = str.split()
    for word in arr:
        c = findRepeats(word)
        if c > greatestCount:
            greatest = word
            greatestCount = c
    return greatest

# print(LetterCount(input()))

def CaesarCipher(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# print(CaesarCipher(input(), int(input())))

def SimpleMode(arr):
    mode_dict = {}  # Create a dictionary to store the occurrences of each element
    max_count = 0   # Variable to keep track of the maximum occurrence
    mode = -1       # Variable to store the mode (initialize as -1 in case there is no mode)

    for num in arr:
        if num in mode_dict:
            mode_dict[num] += 1
        else:
            mode_dict[num] = 1

        # Update the mode and max_count if the current element has a higher occurrence
        if mode_dict[num] > max_count:
            mode = num
            max_count = mode_dict[num]

    # Check if there is no mode (all elements appear once)
    if max_count == 1:
        return -1

    return mode

# print(SimpleMode(input()))

def Consecutive(arr):
    min_num = min(arr)
    max_num = max(arr)
    total_integers = max_num - min_num + 1
    current_integers = len(arr)
    return total_integers - current_integers

# print(Consecutive(input()))