""""Write a function partlist that gives all the ways to divide a list (an array)
of at least two elements into two non-empty parts."""


def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        result.append((' '.join(arr[:i]), ' '.join(arr[i:])))
    return result


in_list = [["I", "wish", "I", "hadn't", "come"], ["cdIw", "tzIy", "xDu", "rThG"], ["vJQ", "anj", "mQDq", "sOZ"]]
out_list = [
    [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"),
     ("I wish I hadn't", "come")],
    [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")],
    [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")]
]


def test():
    for i, lst in enumerate(in_list):
        print(partlist(lst) == out_list[i])


if __name__ == '__main__':
    test()
