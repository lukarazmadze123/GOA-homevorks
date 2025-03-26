def count_positive_numbers(lst):
    return sum(1 for num in lst if num > 0)


sum_if_positive = lambda x, y: x + y if x > 0 and y > 0 else "Invalid"


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(lst):
    return [num for num in lst if is_prime(num)]


def has_vowel(s):
    vowels = "aeiouAEIOU"
    return any(char in vowels for char in s)

def concatenate_if_vowel(str1, str2):
    if has_vowel(str1) and has_vowel(str2):
        return str1 + str2
    return "Cannot concatenate"


def longest_element(lst):
    return max(lst, key=len) if lst else None


print(count_positive_numbers([-2, 5, 10, -8, 0, 3]))
print(sum_if_positive(3, 4))  
print(sum_if_positive(-2, 5))  
print(filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 11]))
print(concatenate_if_vowel("hello", "world"))
print(concatenate_if_vowel("sky", "rhythm")) 
print(longest_element(["apple", "banana", "cherry"]))