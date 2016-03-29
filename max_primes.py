import sys, math, time, os, copy, signal
import multiprocessing as mp
from multiprocessing import Process, Queue
from threading import Thread

def handler(signum, stack):
	print "bye bye"

def timer():
	i = 2
	while i > 0:
		print "You have " + str(i) + " seconds left."
		time.sleep(1)
		i -= 1

	print "You are out of time!"
	os.kill(os.getppid(), signal.SIGUSR1)

def main(args):

	# I am going to use #ratosthenes Sieve but skipping all of the even numbers to save time
	primeSieve = []
	numProcs = mp.cpu_count()

	d = Process(target = timer, args = ())

	d.start()


	primeCeiling = 10
	signal.signal(signal.SIGUSR1, handler)


	# putting a palce holder for 0 and 1
	# I am going to make the indexes of the list
	primeSieve.append(False) #0
	primeSieve.append(False) #1
	primeSieve.append(True) #2

	# Initiate the rest of the Sieve to False to represent untested
	for i in range(0, primeCeiling - 3):
		primeSieve.append(True)

	# start the count at three as we know 2 is a prime number.
	i = 3
	
	while i < primeCeiling:
		z = i
		
		while z < primeCeiling:
			if z / i != 1:
				primeSieve[z] = False
				z = z + i
			else:
				z = z + i

		i = i + 2

	# print out the finished portion of the Sieve
	for i in range(1, primeCeiling):
		if primeSieve[i] == True and i % 2 != 0:
			print i

if __name__ == '__main__':
    main(sys.argv)