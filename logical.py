# a = True
# print("a is", a)
#
# b = a
# print("b is", b)
#
# c = not a    # c is false
# print("c is", c)
#
# d = not b
# print(d)
# e = False
#
# f = True
#
# if a != c:
#     print("yes yes")
#     print("prints a !=c", a != c)
# if e is not c:   # e is false => (false is not false) => false
#     print("e is false, c is false", True)
#
# else:
#     print("e is false, c is false therefore the statement is", False)
#
# if f is not c:  # true is not false
#     print("f is true, c is false, therefore the statement is", True)
#     print(" prints f is not c:", f is not c)
# else:
#     print("FF no no")

# sentences = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
# oneSentence = sentences.split(" ")
# same_letter_count = 0
# print(oneSentence)
# for i in oneSentence:
#     if i[0] == i[-1]:
#         same_letter_count += 1
# print(same_letter_count)

# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
# acc_num = 0
# for i in items:
#     if "w" in i:
#         acc_num += 1
# print(acc_num)

# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
# words = sentence.split(" ")
# num_a_or_e = 0
# for i in words:
#     if "a" in i or "e" in i:
#         num_a_or_e += 1
# print(num_a_or_e)

# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# words = s.split()
# num_vowels = 0
# for i in words:
#     for j in vowels:
#         if j in i:
#             n = i.count(j)
#             num_vowels += n
# print(num_vowels)




# One way to do this is by using the count method on the current word i
# for each vowel j in the inner loop, and adding this count to num_vowels.

# s = "python"
# for idx in range(len(s)):
#     print(idx, idx % 2, s[idx % 2])
#

# f = []
# x = 0
# for i in range(53):
#     f.append(i)
#
# print(f)
# str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
#
# true = str1.find("True")  # 27
# false = str1.find("False")  # -1
# print(true)
# print(false)
# if true > 1:
#     output = "False. You are'nt You?"
# elif false > 1:
#     output = "True! You are you!"
# else:
#     output = "Neither true nor false!"
# print(output)
#Create an empty list called resps.
# Using the list percent_rain, for each percent,
# if it is above 90, add the string ‘Bring an umbrella.’
# to resps, otherwise if it is above 80, add the string
# ‘Good for the flowers?’ to resps, otherwise if it is
# above 50, add the string ‘Watch out for clouds!’ to resps,
# otherwise, add the string ‘Nice day!’ to resps. Note:
# if you’re sure you’ve got the problem right but it
# doesn’t pass, then check that you’ve matched up the strings exactly.
#
# percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
#
# resps = []
#
# for i in percent_rain:
#     if i > 90:
#         resps.append("Bring an umbrella.")
#     elif i > 80:
#         resps.append("Good for the flowers?")
#     elif i > 50:
#         resps.append("Watch out for clouds!")
#     else:
#         resps.append("Nice day!")
# print(resps)

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word.endswith("e"):
        newWord = word + "d"
        past_tense.append(newWord)
    else:
        newWord = word + "ed"
        past_tense.append(newWord)

print(past_tense)
