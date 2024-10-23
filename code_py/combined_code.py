
# Task: lister.py

tall1 = [7, 24, 10, 26, 35, 10, 29, 2, 29, 40, 40, 26, 16, 8, 9, 26, 5, 18, 9, 13, 40, 28, 37, 32, 6, 11, 35, 9, 26, 10, 11, 27, 4, 8, 22, 40, 19]
tall2 = [56, 49, 28, 52, 58, 33, 26, 27, 58, 36, 36, 48, 55, 25, 58, 57, 30, 27, 36, 39, 50, 58, 50, 58, 52, 22, 27, 48, 37, 30, 32, 38, 31, 31, 25, 42, 54]

# a. Remove duplicates from both lists
tall1_no_duplicates = list(set(tall1))
tall2_no_duplicates = list(set(tall2))

print("List 1 without duplicates:", tall1_no_duplicates)
print("List 2 without duplicates:", tall2_no_duplicates)

# b. Find common numbers in both lists
common_numbers = list(set(tall1) & set(tall2))

print("Numbers in both lists:", common_numbers)

# c. Find numbers that are in only one list but not both
unique_to_either_list = list(set(tall1) ^ set(tall2))

print("Numbers only in one list:", unique_to_either_list)


# Task: liste_manipulering.py

# a. Function to concatenate two lists
def vanlig_konkat(list1, list2):
    return list1 + list2

# b. Function to interleave two lists
def annenhver_konkat(list1, list2):
    return [item for pair in zip(list1, list2) for item in pair]

# c. Function to return a list of digits from a number
def tall_til_liste(number):
    return [int(digit) for digit in str(number)]

# Example usage of functions
print(vanlig_konkat(['a', 'b', 'c'], [1, 2, 3]))
print(annenhver_konkat(['a', 'b', 'c'], [1, 2, 3]))
print(tall_til_liste(895))


# Task: inneholder.py

# a. Function to check if all characters of string1 are in string2
def inneholder(str1, str2):
    return all(char in str2 for char in str1)

# Example usage
print(inneholder("hei", "hello"))  # False
print(inneholder("hi", "hi"))      # True

# b. Modify to check character count
from collections import Counter

def inneholder(str1, str2):
    count1, count2 = Counter(str1), Counter(str2)
    return all(count1[char] <= count2[char] for char in count1)

# Example usage
print(inneholder("hei", "heihei"))  # True
print(inneholder("heihei", "hei"))  # False

# c. Anagram function
def anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
print(anagram("lese", "esel"))  # True
print(anagram("les", "esel"))   # False


# Task: matkalender.py

# Function to read meals from a file and suggest based on available time
def les_matretter(filnavn):
    matretter = {}
    with open(filnavn, 'r') as file:
        for linje in file:
            rett, tid = linje.rsplit(',', 1)
            matretter[rett] = int(tid.strip())
    return matretter

def foresla_matrett(matretter, maks_tid):
    forslag = [rett for rett, tid in matretter.items() if tid <= maks_tid]
    return forslag if forslag else "Ingen forslag"

# Example usage
matretter = les_matretter('matretter.txt')
print(foresla_matrett(matretter, 30))  # Suggest meals within 30 minutes
