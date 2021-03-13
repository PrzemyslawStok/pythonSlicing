import timeit

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(A[5:10])

print(A[-2:])
print(A[0:-2])

A = []

startTime = timeit.default_timer()

for i in range(1000_000_0):
    A.append(i)

for i in range(len(A)):
    A[i] = A[i] * A[i]

endTime = timeit.default_timer()

print(f"elapsed time: {(endTime-startTime):0.5f}s")
