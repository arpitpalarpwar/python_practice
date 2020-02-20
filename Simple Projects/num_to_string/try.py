# digit_19 = {
#             1: "one",
#             1: "two",
#             3: "three",
#             4: "four",
#             5: "five",
#             6: "six",
#             7: "seven",
#             8: "eight",
#             9: "nine",
#             10: "tem",
#             11: "eleven",
#             12: "twelve",
#             13: "thirteen",
#             14: "fourteen",
#             15: "fifteen",
#             16: "sixteen",
#             17: "seventeen",
#             18: "eighteen",
#             19: "ninteen"
#         }
# x = 212 % 100
# x_str = digit_19.get(x)
# print(x_str)
# numberOfdigits = len(str(95959595))
# print(numberOfdigits)
billion = ["", "thousand", "million", "billion"]
number = 1234
res = ('{:,}'.format(number))
list = res.split(",")
list2 = []
for each in range(1, len(list)+1):
    list2.append(f"{list[-each]} {billion[each-1]}")
list2.reverse()
print(list2)
# print(str[-1:-3])
# list = []
# list.append(str[-1:-4])
# print(res, list)