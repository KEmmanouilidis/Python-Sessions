# < ---------- Exercise 3 ---------- >
# Using the following list:
# {"pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"}
# Reverse all the letters in each item in the list, and print them. For example, 'pizza" will be 'azzip'.
# < --------------------------------- >


foodlist=["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"]

print("The list's strings, reversed:")
for i in foodlist:
    print(i[::-1])
