#!/bin/usr/python3
"""
Statistical Question 1:
Given following assumptions
- length of the set
- maximum and minimum
- quartils
- standard deviation
- mean

Does a set of whole numbers exist, that fulfils these assumptions?

With this tool you can answer the question, given you don't change following two assumptions
- length of set (10)
- whole numbers
"""
import random
import statistics as stat

class dependencies():
    def __init__(self, List):
        self.List = List

    def setter(self,length,minimum, maximum):
        List = self.setLength(length)
        List = self.setMin(minimum)
        List = self.setMax(maximum)
        return List


    def setLength(self,length):
        for item in range(length):
            self.List.append(item+1)
        return self.List

    def setMin(self,minimum):
        self.List[0] = minimum
        return self.List

    def setMax(self,maximum):
        lenList = len(self.List)
        List[lenList-1] = maximum
        return self.List

    def setQuartileTwin(self,low,quartil):
        high = (2 * quartil ) - low
        return high

    def setMean(self,low,mean, minimum, maximum, q_1,q_2,q_3):
        difference = ( 10 * mean )- (maximum + minimum + 2*(q_1 + q_2 +q_3))
        high = difference - low
        return high


class tests():
    def __init__(self, List):
        self.List = List

    def TestAll(self, mean="?", q_1="?", q_2="?", q_3="?", stdev="?", verbose=False):
        output = ["?","?","?","?","?"]
        if mean != "?":
            if self.testMean(mean):
                output[0] = "Y"
            else:
                output[0] = "N"
                if verbose:
                    print(self.List,output)
                return False
        if q_1 != "?":
            low = self.List[1]
            high = self.List[2]
            if self.testQuartil(low, high, q_1):
                output[1] = "Y"
            else:
                output[1] = "N"
                if verbose:
                    print(self.List,output)
                return False
        if q_2 != "?":
            low = self.List[4]
            high = self.List[5]
            if self.testQuartil(low, high, q_2):
                output[2] = "Y"
            else:
                output[2] = "N"
                if verbose:
                    print(self.List,output)
                return False
        if q_3 != "?":
            low = self.List[7]
            high = self.List[8]
            if self.testQuartil(low, high, q_3):
                output[3] = "Y"
            else:
                output[3] = "N"
                if verbose:
                    print(self.List,output)
                return False
        if stdev != "?":
            if self.testStdev(stdev):
                output[4] = "Y"
            else:
                output[4] = "N"
                if verbose:
                    print(self.List,output)
                return False
        if output == ["Y","Y","Y","Y","Y"]:
            print("WE'VE GOT A WINNER!!!", self.List, output)
            return True

    def testMean(self,mean):
        if stat.mean(self.List) == mean:
            return True
        else:
            return False

    def testQuartil(self,low, high, quartil):
        calcQuartil = ( low + high )/2
        if calcQuartil == quartil:
            return True
        else:
            return False

    def testStdev(self,stdev):
        if stat.pstdev(self.List) == stdev:
            return True
        else:
            return False

class smartFiller():
    def __init__(self, List,quartils):
        self.List = List
        self.quartils = quartils
        self.chain = []
        self.linkedChain = []
        self.key = [0,0,0,0]
        self.step = 0

        q_1 = quartils[0]
        q_2 = quartils[1]
        q_3 = quartils[2]

        n_2range = range(self.List[0],q_1+1)
        n_4range = range(q_1,q_2+1)
        n_5range = range(q_1,q_2+1) # see that n_5>n_4
        n_8range = range(q_2,q_3+1)
        self.ranges = [ n_2range, n_4range, n_5range, n_8range ]

    def fill(self):
        for two in self.ranges[0]:
            self.key[0] = two
            for four in self.ranges[1]:
                self.key[1] = four
                for five in self.ranges[2]:
                    if five < four:
                        continue
                    self.key[2] = five
                    for eight in self.ranges[3]:
                        self.key[3] = eight
                        self.step += 1
                        self.chain.append(list(self.key))
        for link in self.chain:
            self.List[1] = link[0]
            self.List[3] = link[1]
            self.List[4] = link[2]
            self.List[7] = link[3]
            self.linkedChain.append(list(self.List))
        
        for item in self.linkedChain:
            low = item[1]
            high = dep.setQuartileTwin(low, q_1)
            if low < high:
                item[2] = high
            else:
                continue

            low = item[4]
            high = dep.setQuartileTwin(low, q_2)
            if low < high:
                item[5] = high
            else:
                continue

            low = item[7]
            high = dep.setQuartileTwin(low, q_3)
            if low < high:
                if high < item[9]:
                    item[8] = high
                else:
                    continue
            else:
                continue

            low = item[3]
            high = dep.setMean(low, mean, minimum, maximum, q_1,q_2,q_3)
            if low < high:
                item[6] = high
            else:
                continue

            tst = tests(item)
            tst.TestAll(mean, q_1, q_2, q_3, s, verbose=False)


### MAIN
# Set Standards
for i in 4,12,10,8:
    List = []
    length = 10
    mean = 39
    minimum = 2
    maximum = 93
    s = 34
    q_1 = i #12 # this was 4 before
    q_2 = 33
    q_3 = 77

    msg = "Lenght: {}, mean: {}, standard deviation: {}, minimum: {}, maximum: {}, quartils: {} {} {}"
    msg = msg.format(length, mean, s, minimum, maximum, q_1, q_2, q_3)
    print(msg)
    # Helpers
    quartils = [q_1,q_2,q_3]

    # Make List
    dep = dependencies(List)
    List = dep.setter(length, minimum, maximum)

    # Make list of lists
    sf = smartFiller(List,quartils)
    linkedChain = sf.fill()
