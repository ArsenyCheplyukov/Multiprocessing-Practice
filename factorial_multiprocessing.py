from multiprocessing import Process, Value
import timeit # for testing execution time


def multiply_value(val, num):
    # Multiply value by given
    with val.get_lock():
        val.value *= num


def factorial(number):
    shared_value = Value('i', 1)  # Create common for processes value
    processes = []
    for num in range(1, number+1):
        process = Process(target=multiply_value, args=(shared_value, num))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()

    # Value will be updated after all the processes
    return shared_value.value


if __name__ == "__main__":
    n = int(input("Enter value to calculate factorial:\n"))
    print(f"Factorial of this value is: {factorial(n)}")
    for i in [1, 5, 10, 50, 100, 200]:
        print(f"Mean multiprocess calculation of factorial time for {i}:")
        print(timeit.timeit(lambda: factorial(i), number=5)/5, "\n")