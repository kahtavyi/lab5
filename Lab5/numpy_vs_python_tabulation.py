import math
import numpy as np
from matplotlib import pyplot as plt
import time

def f(x: np.ndarray, N: int) -> np.ndarray:
    """
    Calculate function values for passed array of arguments
    """
    return np.sin(np.pi * x * N)

def tabulate(a: float, b: float, n: int, N: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Tabulate the function using Python lists
    """
    x = [a + x * (b - a) / n for x in range(n)]
    y = f(np.array(x), N)
    return np.array(x), y

def tabulate_numpy(a: float, b: float, n: int, N: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Tabulate the function using NumPy
    """
    x = np.linspace(a, b, n)
    y = f(x, N)
    return x, y

def main():
    N = 13

    # Tabulate using Python lists
    start_time = time.time()
    res_python = tabulate(0, 1, 1000, N)
    end_time = time.time()
    python_time = end_time - start_time

    # Tabulate using NumPy
    start_time = time.time()
    res_numpy = tabulate_numpy(0, 1, 1000, N)
    end_time = time.time()
    numpy_time = end_time - start_time

    # Plotting results
    plt.plot(res_python[0], res_python[1], label='Python Lists')
    plt.plot(res_numpy[0], res_numpy[1], label='NumPy')
    plt.grid()
    plt.legend()
    plt.show()

    # Comparing results
    print("Time taken for tabulation using Python lists:", python_time)
    print("Time taken for tabulation using NumPy:", numpy_time)

if __name__ == '__main__':
    main()

