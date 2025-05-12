import time
import math

x = 2
y = 2.5

start = time.perf_counter()
_ = x ** y
duration = time.perf_counter() - start
print(f"** süresi:  {duration:.10f} saniye")

start2 = time.perf_counter()
_2 = math.pow(x, y)
duration2 = time.perf_counter() - start2
print(f"pow süresi: {duration2:.10f} saniye")