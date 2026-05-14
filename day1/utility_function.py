#1 find max value
def find_max(arr):
    if not arr:
        return None
    max_value = arr[0]
    for n in arr:
        if n > max_value:
            max_value = n
    return max_value

#2 reverse a string
def reverse_string(s):
    return s[::-1]

#3 check palindrome
def is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    return s == reverse_string(s)

#4 remove duplicates from a list
def remove_duplicate(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result

#5 calculate frequencies in a list
def calculate_frequencies(list):
    freq = {}
    for item in list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

if __name__ == "__main__":
    print(find_max([3, 1, 4, 1, 5, 9]))
    print(reverse_string("Hello, World!"))
    print(is_palindrome("tenet"))
    print(remove_duplicate([1, 2, 2, 3, 4, 4, 5]))
    print(calculate_frequencies([1, 2, 2, 3, 4, 4, 4, 5]))