#
# COSC 240 - ALGORITHMS - 5 numbers of an array that sum to zero
# Troy Holland
#
# algorithm combines the solution for 3 and 4 numbers that sum to zero as gone over in class
# have original array of size n; create "two" arrays of size n^2; for each number i in array,
# see if sums k and j (from sum arrays) are equivalent to -i; if not, increment or decrement
# index in one of the arrays (based on situation); if equivalent, check if all of the used
# numbers are unique; if not, move index in one of the arrays, else, found 5 numbers that sum to zero
#

sumArray = []
myArray = [-10, 0, -8, 11, 9, 14, -2, 3, 5, -17, -4, 1, -1]

#creates 'array of arrays' that holds sums of all permutations of 2 numbers from original array
def getAllSums(sizeArray):
	for x in range(0, sizeArray): #go through original array
		for y in range(x, sizeArray): #get number to pair with
			if(myArray[x] != myArray[y]): #only perform addition if two UNIQUE numbers
				sumArray.append([myArray[x] + myArray[y], myArray[x], myArray[y]])
			
	#sort when done - sorts by first element in 3-element array inside each element of the created array
	sumArray.sort()
	
#sees if 5 numbers are unique and do not overlap
def ifUnique(sumOne, sumTwo, value):
	if(sumOne[1] != sumTwo[1] and sumOne[1] != sumTwo[2] and sumOne[2] != sumTwo[1] and sumOne[2] != sumTwo[2]
	and value != sumOne[1] and value != sumOne[2] and value != sumTwo[1] and value != sumTwo[2]):
		return True
	else:
		return False
	
#called on original array, main algorithm
def findIfEqualZero(sizeArray, sizeSumArray):
	if(sizeArray == 5):
		if(sum(myArray) == 0):
			print "Found: "
			print myArray
		else:
			print "Not Found"
	elif(sizeArray < 5):
		print "Not possible"
	else:
		for x in range(0, sizeArray): #go through each number in original sorted array - n run time
			if(findIfEqualOpp(x, sizeSumArray)): #go through sum arrays and find 2 sums whose sum is the opposite value in original array
				return True
			else:
				return False
			
	#############################################
	# n * n^2 = n^3 total run time of algorithm #
	#############################################	
#going through the sum array
def findIfEqualOpp(indexMyArray, sizeSumArray):
	oppValue = -1 * myArray[indexMyArray]

	#set up "two" arrays
	startSumArray = 0
	endSumArray = sizeSumArray - 1
	
	#go through "two" arrays
	while(startSumArray < sizeSumArray and endSumArray >= 0): # n^2 run time
		#if sum of sums is the same value as the opposite of current value in original array
		if((sumArray[startSumArray][0] + sumArray[endSumArray][0] == oppValue) and ifUnique(sumArray[startSumArray], sumArray[endSumArray], 
		myArray[indexMyArray])):
			print "Found:" 
			print sumArray[startSumArray][1], sumArray[startSumArray][2], sumArray[endSumArray][1], sumArray[endSumArray][2], myArray[indexMyArray]
			return True
		elif(sumArray[startSumArray][0] + sumArray[endSumArray][0] < oppValue): #increment "first" array
			startSumArray = startSumArray + 1
		else: #increment "second" array - **takes care of the problem if numbers overlap**
			endSumArray = endSumArray - 1
	
def main():
	sizeArray = len(myArray)

	#sort array
	myArray.sort()
	
	#produce sorted arrays of all sums
	getAllSums(sizeArray)
	sizeSumArray = len(sumArray)
	
	#run algorithm
	found = findIfEqualZero(sizeArray, sizeSumArray)
	
	if(found == False):
		print "Not Found"

if __name__ == "__main__":
	main()