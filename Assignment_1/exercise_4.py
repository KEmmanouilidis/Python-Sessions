# < ---------- Exercise 4 ---------- >
# Store the results of exercise 2 to a dictionary and print it.
# The dictionary should look like this:
# letters = {'a': 9, 'e': 4, ...}
# < --------------------------------- >

foodlist = ["pizza", "loukoumades" ,"melomakarona" ,"kourampiedes" ,"tzaziki" ,"paidakia"]
letters = ["a","e","i","o","u"]

omydict = {}

for i in letters:  # iterating starting from the first item of the letters list
    k = 0  # variable set to 0 - assists later - check the if condition.
    for j in foodlist:  # continuing to the first item of food list
        for character in j:  # continuing to each character of each item in foodlist (first character "p")
            if i in character:  # if the item of the letters list is in - or equals to - the character of the item of foodlist then do:
                k += 1  # increase variable each time an item of letters exists in a character of an item of foodlist
                omydict[i] = k  # set new keys and values to a dictionary (omydict[a]="1", omydict[a]="2" etc.)
print(omydict)
