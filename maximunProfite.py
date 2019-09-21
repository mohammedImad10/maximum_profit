import random


def maximumProfit(price):
    # Write your code here
    final = 0
    numOfElement = 0
    counter = 0
    for i in range(price.__len__()):
        print(i)
        if i == price.__len__() - 1:
            print("---" + (str)(i))
            if price[i] > price[i - 1]:
                final = final + price[i] * numOfElement
                numOfElement = 0
                break
        else:
            print("-else--" + (str)(i))
            if i == 0:
                if price[i] < price[i + 1]:
                    numOfElement = numOfElement + 1
                    final = final - price[i]
            else:
                if price[i] < price[i + 1]:
                    numOfElement = numOfElement + 1
                    final = final - price[i]
                else:
                    final = final + price[i] * numOfElement
                    numOfElement = 0



    return final


def main():

     print("***"+str(maximumProfit([100,3,4,5])))



if __name__ == '__main__': main()