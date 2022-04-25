"""John wants to decorate the walls of a room with wallpaper. He wants a fool-proof method for getting it right.
John knows that the rectangular room has a length of l meters, a width of w meters, a height of h meters.
The standard width of the rolls he wants to buy is 52 centimeters. The length of a roll is 10 meters.
He bears in mind however, that it’s best to have an extra length of wallpaper handy in case of mistakes or
miscalculations so he wants to buy a length 15% greater than the one he needs.
Last time he did these calculations he got a headache, so could you help John?
Task
Your function wallpaper(l, w, h) should return as a plain English word in lower case the number of rolls he must buy."""


def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    if l == 0 or w == 0 or h == 0:
        n = 0
    else:
        l *= 100
        w *= 100
        h *= 100
        n = int((2.3 * h * (l + w)) / 52000) + 1
    return numbers[n]


def testing(func, value: str) -> bool:
    """test function"""
    print(func == value)


testing(wallpaper(6.3, 4.5, 3.29), "sixteen")
testing(wallpaper(7.8, 2.9, 3.29), "sixteen")
testing(wallpaper(6.3, 5.8, 3.13), "seventeen")
testing(wallpaper(6.1, 6.7, 2.81), "sixteen")
