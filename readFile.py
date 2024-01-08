# file = open('mbox-short.txt', 'r')
# counter = 0
# collected = []
# nums = 0
# ave = 0
# for line in file:
#     if line.startswith('X-DSPAM-Confidence: '):
#         collected.append(float(line.rstrip().lstrip('X-DSPAM-Confidence: ')))
# print(collected)
# for i in collected:
#     nums += i
#     ave = nums / len(collected)
# print("ave is: ", ave)

#
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# splited = org.split()
# acro = ""
# print(splited)
# for i in splited:
#     if i not in stopwords:
#         acro += i[0].upper()
#
# print(acro)


# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
# sent = "The water earth and air are vital"
#
# splited = sent.split()
# acro = ""
# print(splited)
# for i in splited:
#     if i not in stopwords:
#         acro += i[0:2].upper() + ". "
#         acro.rsplit(". ")
# print(acro)
#
#
# flipped = stopwords.reverse()
# print(flipped)

# p_phrase = "was it a car or a cat I saw"
# r_phrase = ""
#
# for word in p_phrase.split():
#     r_phrase += word[::-1] + " "
# print(r_phrase)
#


# fname = input("Enter file name: ")
# fh = open(fname, "r")
# lst = list()
# poem = fh.read().split("\n")
#
# for sentences in poem:
#     words = sentences.split()
#     for word in words:
#         if word not in lst:
#             lst.append(word)
#
# lst.sort()
# print(lst)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lines = fh.readlines()
for line in lines:
    if line.startswith("From "):
        email = line.split()
        print(email[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
