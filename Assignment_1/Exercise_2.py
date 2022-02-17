# < ---------- Exercise 2 ---------- >
# Using the same list above,
# print out the number of times each of the following letters appears:
# a, e, i, o and u, in the items of the list (total count for all the items).
# Like this
# The letter 'a' appears 9 times
# The letter 'e' appears 4 times
# etc..
# < --------------------------------- >

foodlist=["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"]
letters=["a", "e", "i", "o", "u"]

# detailed comments for the below under exercise 4
for i in letters:
    k=0
    for j in foodlist:
        for character in j:
            if i in character:
                k+=1
    print("The letter '{}' appears {} times".format(i,k))
