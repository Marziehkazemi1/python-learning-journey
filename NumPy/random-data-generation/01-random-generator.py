import numpy as np

rng = np.random.default_rng()
numbers = rng.integers(1, 10, size=5)
print(numbers)

#The random output is repeatable across different runs.
#Generate a sequence of pseudo-random numbers each time from a given starting point ===> for exm 42
rng1 = np.random.default_rng(42)
print(rng1.integers(1, 100, size=(2, 3)))    #size  ==> generate matrix 2*3

#integers() — random integers
rng2 = rng.integers(low=1, high=10, size=5, endpoint=True)     #endpoint=True: Includes the upper limit in the range.
print("rng2:", rng2)

#random() — Random decimal numbers
rng3 = rng.random(size=5)
print("rng3:", rng3)

numbers = 10 + 10 * rng.random(size=5)    #generate random numbers between 10, 20
print("numbers:", numbers)

#uniform() — Uniform distribution
rng4 = rng.uniform(low=10, high=20, size=5)
print("rng4:", rng4)

#choice() — Random selection from data
data = np.array([10, 20, 30, 40, 50])
print("data:", rng.choice(data))
print("data 3:", rng.choice(data, size=3))
print("replace=False", rng.choice(data, size=3, replace=False))
print("replace=True", rng.choice(data, size=3, replace=True))

#bytes() — Produce byte data
rng5 = rng.bytes(8)
print("rng5:", rng5)

#shuffle() — Change the order of the same array
a = np.array([1, 2, 3, 4, 5])
rng.shuffle(a)
print("a:", a)

#permutation() — Return a new random permutation
b = np.array([1, 2, 3, 4, 5])
c = rng.permutation(b)
print("b:", b)
print("c:", c)

#permuted() — Independent permutation along an axis
d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("d axis0:", rng.permuted(d, axis=0))
print("d axis1:", rng.permuted(d, axis=1))

#normal() — Normal distribution
#loc: mean
#scale: standard deviation; must be nonnegative
#size: number or shape of output
rng6 = rng.normal(loc=100, scale=15, size=5)
print("rng6:", rng6)

#standard_normal() - standard Normal distribution
#Numbers are generated from a distribution with a mean of zero and a standard deviation of one.
rng7 = rng.standard_normal(size=5)
print("rng7:", rng7)

#standard_t() — Student's t-distribution
rng8 = rng.standard_t(df=5, size=5)
print("rng8:", rng8)

#binomial() — Binomial distribution
rng9 = rng.binomial(n=10, p=0.3, size=5)
print("rng9:", rng9)

#poisson() — Poisson distribution
rng10 = rng.poisson(lam=4, size=5)
print("rng10:", rng10)

#exponential() — Exponential distribution
rng11 = rng.exponential(scale=2, size=5)
print("rng11:", rng.exponential(scale=2, size=5))