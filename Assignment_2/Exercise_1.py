# <----------------------------------------------------------------------------------------------->
# Create a class named List_Mean that has the following:

# (1) A class variable that contains a list of numbers.
# (2) A class method "set_list" for setting the value of the class variable.
# (3) A class method "get_list" for getting the class variable.
# (4) A class method "calc_avg" that returns the Average(mean) of the numbers in the list.

# Test your class with the following two lists (submit the test program):

# [1,2,17,52.5, 43, 4.4, 10]
# [1,2,3,4,5,6,7,"dog"]
# <----------------------------------------------------------------------------------------------->
# Notes/ to study (pending):
# - class variables & class instances
# - Decorators
# - __init__ method
# - Private & public methods
# - Class/ static/ instance methods
# <----------------------------------------------------------------------------------------------->

class ListMean:

    listvalue=[]

    # Initializing / setting the value of the class variable (listvalue)
    def setlist(self,listvalue):
        self.listvalue=listvalue


    # Method to print/return the list value(?)
    def getlist(self):
        return self.listvalue

    # Method to calc the variable's (list's) AVG.
    def calcavg(self):
        nonnumerical = False
        # Checking if there is a string in the given instance
        for i in self.listvalue:
            if type(i)==str:
                nonnumerical = True
         # If there is a string then remove all strings & print the newly formatted list
        if nonnumerical == True:
            #  Iterate through a copy list (which is intact) and remove items only from the original one
            #  Iterating on the original list and removing items at the same time causes issues
            for i in list(self.listvalue):
                if type(i) == str:
                    self.listvalue.remove(i)
            print("The non-numerical values have been removed & the new list is:{}".format(self.listvalue))
            return("The average of the new list is: {}".format((sum(self.listvalue) / len(self.listvalue))))
        # If no strings were found in the list then calc avg
        else:
            return("The list is: {} and the average is {}".format((self.listvalue),(sum(self.listvalue) / len(self.listvalue))))



#testing the class with the 1st list [1st object]
myList1=ListMean()
myList1.setlist([1,2,17,52.5, 43, 4.4, 10])
myList1.getlist()
print(myList1.calcavg())

#testing the class with the 2nd list [2nd object]
myList2=ListMean()
myList2.setlist([1,2,3,4,5,6,7,"dog"])
myList2.getlist()
print(myList2.calcavg())
