# < ---------- Exercise 1 ---------- >
# Using the following list:
# {"pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"}
# Using a loop, print each item individually (one item per line) and then count and print the total number of items like this:
# Total number of items = 4
# < --------------------------------- >

foodlist=["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"]

for i in foodlist:
    print(i)
print("Total number of items = {}".format(len(foodlist)))
