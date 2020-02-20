def stringOf3(num):
    string = ""
    digit_19 = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "tem",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "ninteen"
    }
    digit_post_20 = {
        2 : "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninty",
        1: "hundered"
    }
    if num > 99 and num < 1000:
        last2 = num%100
        if last2 <= 19:
            string = f"{num//100} hundred {digit_19.get(last2)}"
        elif last2 > 19:
            last1 = last2%10
            secondlast = last2//10
            string = f'{digit_19.get(num//100)} hundred {digit_post_20.get(secondlast)} {digit_19.get(last1)}'
        return string.upper()
    elif num > 0 and num <= 99:
        if num <= 19:
            return digit_19.get(num).upper()
        elif num > 19:
            return f"{digit_post_20.get(num//10)} {digit_19.get(num % 10)}".upper()


def stringOfBillion(num):
    if num <= 8000000000:
        billion = ["", "thousand", "million", "billion"]
        res = ('{:,}'.format(num))
        list = res.split(",")
        list2 = []
        for each in range(1, len(list) + 1):
            list2.append(f"{stringOf3(int(list[-each]))} {billion[each - 1]}")
        list2.reverse()
        string = ""
        for each in list2:
            string += each+" "
        string.strip()
        # string.rstrip(",")
        return string.title()

print(stringOfBillion(999889999))

