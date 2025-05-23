# def longest_word(sentence):
#     max_word = ""
#     current_word = ""

#     for character in sentence:
#         if character == " ":
#             if len(current_word) > len(max_word):
#                 max_word = current_word
#             current_word = ""
#         else:
#             current_word += character

#     if len(current_word) > len(max_word):
#         max_word = current_word

#     return max_word

# sentence = "The quick brown fox"
# print(longest_word(sentence))

# def longest_word(sentence):
#     max_word = ""
#     current_word = ""

#     for char in sentence:
#         if char == " ":
#             if len(current_word) > len(max_word):
#                 max_word = current_word
#             current_word = ""
#         else:
#             current_word += char

#     if len(current_word) > len(max_word):
#         max_word = current_word

#     return max_word

# sentence = "A quick brown fox"
# print(longest_word(sentence))

def longest_word(sentence):
    max_word = ""
    current_word = ""

    for char in sentence:
        if char == " ":
            if len(current_word) > len(max_word):
                max_word = current_word
            current_word = ""
        else:
            current_word += char

    if len(current_word) > len(max_word):
        max_word = current_word

    return max_word

sentence = "A quick brown fox"
print(longest_word(sentence))