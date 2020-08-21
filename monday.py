# quick sort
from random import randint

def quickSortCall(anArray):
    quickSort(anArray, 0, len(anArray)-1)


def quickSort(anArray, lowIndex, highIndex):
    if lowIndex < highIndex:  # if the list is done being sorted this will be false
        p = partition(anArray, lowIndex, highIndex)
        quickSort(anArray, lowIndex, p - 1)  # left side
        quickSort(anArray, p + 1, highIndex)  # right side


def partition(anArray, lowIndex, highIndex):  # takes the list, low index, and high index
    pivotIndex = getPivotIndex(anArray, lowIndex, highIndex)
    pivotVal = anArray[pivotIndex]
    # put pivot at the beginning
    anArray[pivotIndex], anArray[lowIndex] = anArray[lowIndex], anArray[pivotIndex]
    count = lowIndex + 1

    for i in range(lowIndex, highIndex + 1):
        if anArray[i] < pivotVal:
            anArray[i], anArray[count] = anArray[count], anArray[i]  # if a value is found to be lower than the pivot val, it's swapped with the count so that it's on the left side
            count += 1  # increment the count
#    if count != lowIndex + 1 and anArray[count] != pivotVal:  # if count != lowIndex + 1 and anArray[count] != pivotVal:
    anArray[lowIndex], anArray[count-1] = anArray[count-1], anArray[lowIndex]  # swaps the count and the index
    return count-1  # returns the count variable which at this point contains the index location of the pivot


def getPivotIndex(anArray, lowIndex, highIndex):  # takes the list, low index, high index. returns median
    mid = (highIndex - lowIndex) // 2
    pivot = highIndex
    if anArray[lowIndex] < anArray[mid] < anArray[highIndex] or anArray[highIndex] < anArray[mid] < anArray[lowIndex]:
        pivot = mid
    elif anArray[mid] < anArray[lowIndex] < anArray[highIndex] or anArray[highIndex] < anArray[lowIndex] < anArray[mid]:
        pivot = lowIndex
    return pivot


def createArray(size=10, max=50):
    return [randint(0, max) for _ in range(size)]


a = createArray()
print("unsorted: " + str(a))
quickSortCall(a)
print("sorted: " + str(a))
