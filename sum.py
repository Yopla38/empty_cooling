import numpy as np
import time


def faster_sum(y):
 return np.sum(y)

def main():
 y = np.random.rand(100000000)
 start = time.time()
 sum(y)
 end = time.time()
 print(f"Elasped time: {end - start}")
 start = time.time()
 faster_sum(y)
 end = time.time()
 print(f"Elasped time: {end - start}")

if __name__ == "__main__":
  main()
