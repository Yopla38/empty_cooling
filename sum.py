import numpy as np
import time

def sum(y):
  """Return the sum of all elements in array `y`."""
  result = 0
  for yi in y:
    result += yi
  return result

def main():
  y = np.random.rand(100000000)
  start = time.time()
  sum(y)
  end = time.time()
  print(f"Elasped time: {end - start} seconds")

if __name__ == "__main__":
  main()
