import threading

def worker(number):
    try:
        print(f"Thread {number} is running.")
        if number == 3:
            raise ValueError("Oops! Thread 3 encountered an error.")
    except Exception as e:
        print(f"Exception in thread {number}: {e}")

try:
    n = int(input("Enter number of threads to create: "))
    threads = []

    for i in range(n):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads completed.")

except ValueError:
    print("Please enter a valid number.")
import threading

def worker(number):
    try:
        print(f"Thread {number} is running.")
        if number == 3:
            raise ValueError("Oops! Thread 3 encountered an error.")
    except Exception as e:
        print(f"Exception in thread {number}: {e}")

try:
    n = int(input("Enter number of threads to create: "))
    threads = []

    for i in range(n):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads completed.")

except ValueError:
    print("Please enter a valid number.")
