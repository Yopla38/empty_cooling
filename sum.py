import numpy as np
import time
def sum(y):
res = 0
for yi in y:
res += yi4
return res


def main():
 y = np.random.rand(100000000)
 start = time.time()
 sum(y)
 end = time.time()
 print(f"Elasped time: {end - start}")


if __name__ == "__main__":
  main()
