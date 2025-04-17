def replace_vowels(string, replace_char):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char in vowels:
            result += replace_char
        else:
            result += char
    return result

input_string = "hello world"
replacement_char = "#"
print("String after replacing vowels:", replace_vowels(input_string, replacement_char))