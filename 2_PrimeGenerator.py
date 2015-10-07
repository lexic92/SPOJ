'''
Following the algorithm from Wikipedia: Sieve of Eratosthenes.
'''
class PrimeGenerator():

	def main(this):
		#CLASS MEMBER VARIABLES
		this.listOfConsecutiveIntegers = []
		this.p = 2
		this.listOfPrimes = []
		this.MAXIMUM_PRIME_NUMBER = 1000000
		this.debug = True

		#------------------------------------------------------
		#Use Sieve of Eratosthenes to generate a list of primes.
		#------------------------------------------------------
		if this.debug: print "Doing step 1 and 2..."
		this.step1and2()
		if this.debug: print "Doing step 3..."
		this.step3()
		if this.debug: print "Doing step 4..."
		endOfList = this.step4()
		if this.debug: print "Entering while loop for steps 3 and 4..."
		while not endOfList:
			this.step3()
			endOfList = this.step4()

		if this.debug: print "Removing the Nones..."
		# Remove the "Nones", leaving a list of prime numbers in ascending order remaining.
		for x in this.listOfConsecutiveIntegers:
			if x is not None:
				this.listOfPrimes.append(x)


		#------------------------------------------------------
		#Run Test Cases.
		#------------------------------------------------------

		if this.debug: numberOfTestCases = int(raw_input("Enter number of test cases: "))
		else: numberOfTestCases = int(raw_input())

		#Stop after completing the number of test cases.
		for x in range(0, numberOfTestCases):
			if this.debug: line = raw_input("Enter the range, anywhere between 1 and " + str(this.MAXIMUM_PRIME_NUMBER) + " (for example, \"1 10\"): ")
			else: line = raw_input()
			listOfNumbers = line.split()

			#1 <= m <= n <= this.MAXIMUM_PRIME_NUMBER  and n-m<=100000
			m = int(listOfNumbers[0])
			n = int(listOfNumbers[1])

			if this.debug: print "Primes between " + str(m) + " and " + str(n) + ":"
			y = 0
			while y < len(this.listOfPrimes):
				#If it is less than the lower limit
				currentPrimeNumber = this.listOfPrimes[y]
				if (currentPrimeNumber >= m) and (currentPrimeNumber <= n):
					print str(currentPrimeNumber)
				y += 1
			print "" #delimiter between test cases
	'''
	Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
	'''
	def step1and2(this):
		for x in range(0, this.MAXIMUM_PRIME_NUMBER + 1):
			this.listOfConsecutiveIntegers.append(x)
		#2. Initially, let p equal 2, the first prime number.
		# --- already taken care of ----



	'''
	Starting from p, enumerate its multiples by counting to n in increments of p,
	 and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself
	 should not be marked).
	'''
	def step3(this):
		index = 2
		while True:
			if (this.p * index) > this.MAXIMUM_PRIME_NUMBER:
				break
			this.listOfConsecutiveIntegers[this.p * index] = None
			index += 1

	'''
	Find the first number greater than p in the list that is not marked. If
	there was no such number, stop. Otherwise, let p now equal this new number
	(which is the next prime), and repeat from step 3.
	'''
	def step4(this):
		index = this.p + 1
		endOfList = False
		while True:
			if this.p > this.MAXIMUM_PRIME_NUMBER:
				endOfList = True
				break
			if this.listOfConsecutiveIntegers[index] != None:
				this.p = this.listOfConsecutiveIntegers[index]
				break
			this.p += 1
		return endOfList


if __name__ == '__main__':
	primeGenerator = PrimeGenerator()
	primeGenerator.main()