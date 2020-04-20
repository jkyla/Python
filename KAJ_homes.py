#Function to get the prices of home from user
def getHomePrices(priceList):
    price = 0
    while True:
        price = float(input('Enter cost of one home or -99 to quit: '))
        if price == -99:
            break
        else:
            priceList.append(price)

#Function to sort the list of prices
def sortList(priceList):
    n = len(priceList)
    for i in range(0,n-1,1):
        for j in range(0,n-1-i,1):
            if priceList[j]>priceList[j+1]:
                temp = priceList[j]
                priceList[j] = priceList[j+1]
                priceList[j+1] = temp

#Function to calculate average cost of home
def averageCost(priceList):
    index=0
    total=0
    while index<len(priceList):
        total = total + priceList[index]
        index = index + 1
    average = total/index;
    return average

#Function to calculate median cost of home
def medianCost(priceList):
    n = len(priceList)
    #check for even case
    if (n % 2 == 0):
        return (priceList[int(n/2)-1] + priceList[int(n/2)])/2
    else:
        return priceList[int((n+1)/2)-1]

#Function to determine minimum and maximum cost of home
def determineMaxMin(priceList):
    maximum = priceList[0]
    minimum = priceList[0]
    index=0
    while index<len(priceList):
        if priceList[index]>maximum:
            maximum = priceList[index]
        if priceList[index]<minimum:
            minimum = priceList[index]

        index = index + 1

    return maximum, minimum
       
def main():
    #Creating empty list
    priceList = list()

    #Displaying heading
    print('\t\tReal Estate Values')
    print('*********************************************')

    #Calling function to get the prices of home
    getHomePrices(priceList)

    #Calling function to sort the price list
    sortList(priceList)

    print('*********************************************')

    #Printing sorted list
    print('Prices of homes in your area:')
    print(priceList)
    

    print('*********************************************')

    #Calling function to determine median cost of home
    median = medianCost(priceList)
    #Printing median cost of home
    print('The median value is $', median)

    #Calling function to calculate average cost of home
    average = averageCost(priceList)
    #Printing average cost of home
    print('The average sale price is $', average)

    #Calling function to determine highest and lowest price of home
    maximum, minimum = determineMaxMin(priceList)
    #Printing highest and lowest price of home
    print('The minimum sale price is $', minimum)
    print('The maximum sale price is $', maximum)


#Calling main() function
main()

