string = "   hello   "
string2 = "world"

# print(string + string2)
#
# print(string + " " + string2)
# print("I am done!")
upper = string.upper()
# print(string, upper)
#
lower = upper.lower()
# print(upper, lower)
#
# print(string.capitalize())
# if "l" in string:
#     print(True)

# for n in string:
#     print(n)
#     if n in "l":
#         print("yes")
#     elif n == "o":
#         print("no")
# if string > upper:
#     print(True)
# if lower < upper:
#     print(False)
# if lower > lower.capitalize():
#     print("No")

pos = string.find("r")
print(pos)
string3 = string.replace("ll", "yu")
print(string3)
print(string.lstrip(), "string")
print(string.rstrip(), "string2")
print(string.strip(), "string3")
