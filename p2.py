import math
from euler import fibonacci

print sum(fib for fib in fibonacci(4000000) if fib%2 == 0)
