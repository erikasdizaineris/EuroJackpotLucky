import random

# creates 5 unique elements from 1..50 and adds a + and a [0-19]+1 number
count = 0
while (count < 6):
    count = count + 1
    not_so_random = [49, 35, 20, 7, 18, 19, 41, 34, 17, 38, 39, 46, 15, 43, 6, 9, 16, 32]
    randlist = random.sample(not_so_random, 5) + [ "+", random.sample(range(1, 12), 1), "+", random.sample(range(1, 12), 1)]
    nums = list(range(0, 9))
    random.shuffle(nums)
    five_nums = nums[:5]
    print("               ")
    print("Lucky numbers:          {} {} {} {} {} {} {} {} {}".format(*randlist))
    print("Joker lucky numbers: {} {} {} {} {}".format(*five_nums))
    print("###############")

else:
    print("Good luck!")