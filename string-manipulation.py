# string = 'lemon drop'
# print(string[2])
#
# upper = string.upper()
# print(upper)
#
#
# def capitalize_at(word: object, index: int) -> object:
#     return word[:index] + word[index].upper() + word[index + 1:]
#
#
# lemon_drop = capitalize_at(string, 4)
# print(lemon_drop)
# # from 0-2 not including 3
#
# index = string[:3]
# print(index)
#
text = "X-DSPAM-Confidence:    0.8475"

index = text.find(" ")
index2 = text.find("0")
print(index, index2)
number = text[index2:]
print(number)
print("hello world")
# <editor-fold desc="Description">
# text = "string"
# </editor-fold>
# type(text)
# region Description
#
# endregion
# replaced = text.replace("t", "RR")
# print(replaced)
# print(text)
# if text == text.startswith("S"):
#     print(True)
# else:
#     print(False)