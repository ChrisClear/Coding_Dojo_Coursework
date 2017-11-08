"""
Optional Assignment: Foo and Bar
Write a program that prints all the prime numbers and all the
perfect squares for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether
it is prime or a perfect square. If it is a prime number print "Foo".
If it is a perfect square print "Bar". If it is neither print "FooBar".

Do not use the python math library for this exercise. For example,
if the number you are evaluating is 25, you will have to figure out
if it is a perfect square. It is, so print "Bar".

This assignment is extra challenging!
Try pair programming and pulling up a white board.
"""
#pylint: disable-msg=C0103

start = 100
end = 100000
currnum = start

def primes(n=100000):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    print [2] + [i for i in xrange(3, n, 2) if sieve[i]]
